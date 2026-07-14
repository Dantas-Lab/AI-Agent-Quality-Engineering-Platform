from fastapi import APIRouter

from app.llm.fake_llm import FakeLLM
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

fake_llm = FakeLLM()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = fake_llm.generate_response(request.message)

    return ChatResponse(
        answer=answer,
        sources=[],
        session_id=request.session_id,
    )
