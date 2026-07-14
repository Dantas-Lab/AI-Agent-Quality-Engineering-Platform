from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.repositories.conversation_repository import (
    ConversationRepository,
)
from app.llm.factory import create_llm
from app.observability.correlation import generate_correlation_id
from app.observability.events import (
    CHAT_REQUEST_RECEIVED,
    RESPONSE_GENERATED,
    RETRIEVAL_COMPLETED,
)
from app.observability.logger import get_logger
from app.rag.pipeline import RAGPipeline
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import Retriever
from app.rag.vector_store import VectorStore
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()
logger = get_logger()

vector_store = VectorStore()
retriever = Retriever(vector_store)
prompt_builder = PromptBuilder()
llm = create_llm()

rag_pipeline = RAGPipeline(
    retriever=retriever,
    prompt_builder=prompt_builder,
    llm=llm,
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: DatabaseSession,
) -> ChatResponse:
    correlation_id = generate_correlation_id()

    logger.info(
        CHAT_REQUEST_RECEIVED,
        correlation_id=correlation_id,
        session_id=request.session_id,
    )

    repository = ConversationRepository(db)

    conversation = repository.get_or_create_conversation(request.session_id)

    repository.create_message(
        conversation_id=conversation.id,
        role="user",
        content=request.message,
    )

    answer, documents = rag_pipeline.run(request.message)

    logger.info(
        RETRIEVAL_COMPLETED,
        correlation_id=correlation_id,
        document_count=len(documents),
        sources=[document.source for document in documents],
    )

    repository.create_message(
        conversation_id=conversation.id,
        role="assistant",
        content=answer,
    )

    logger.info(
        RESPONSE_GENERATED,
        correlation_id=correlation_id,
        session_id=request.session_id,
    )

    return ChatResponse(
        answer=answer,
        sources=[document.source for document in documents],
        session_id=request.session_id,
    )
