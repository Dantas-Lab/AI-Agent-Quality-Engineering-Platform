from sqlalchemy.orm import Session

from app.database.models import Conversation, Message


class ConversationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_or_create_conversation(self, session_id: str) -> Conversation:
        conversation = (
            self.db.query(Conversation)
            .filter(Conversation.session_id == session_id)
            .first()
        )

        if conversation is None:
            conversation = Conversation(session_id=session_id)
            self.db.add(conversation)
            self.db.commit()
            self.db.refresh(conversation)

        return conversation

    def create_message(
        self,
        conversation_id: int,
        role: str,
        content: str,
    ) -> Message:
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message
