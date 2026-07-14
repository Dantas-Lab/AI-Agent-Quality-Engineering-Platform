from sqlalchemy import func, select

from app.database.connection import SessionLocal
from app.database.models import Conversation, Message


def validate_database() -> None:
    with SessionLocal() as db:
        conversation_count = db.scalar(select(func.count()).select_from(Conversation))

        message_count = db.scalar(select(func.count()).select_from(Message))

        print(f"Conversations: {conversation_count}")
        print(f"Messages: {message_count}")


if __name__ == "__main__":
    validate_database()
