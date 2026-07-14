from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.repositories.conversation_repository import (
    ConversationRepository,
)
from app.llm.fake_llm import FakeLLM
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

fake_llm = FakeLLM()

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: DatabaseSession,
) -> ChatResponse:
    repository = ConversationRepository(db)

    conversation = repository.get_or_create_conversation(request.session_id)

    repository.create_message(
        conversation_id=conversation.id,
        role="user",
        content=request.message,
    )

    answer = fake_llm.generate_response(request.message)

    repository.create_message(
        conversation_id=conversation.id,
        role="assistant",
        content=answer,
    )

    return ChatResponse(
        answer=answer,
        sources=[],
        session_id=request.session_id,
    )
