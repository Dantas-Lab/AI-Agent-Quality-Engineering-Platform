from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

from app.api.routes.chat import router as chat_router  # noqa: E402
from app.api.routes.health import router as health_router  # noqa: E402
from app.database import models  # noqa: E402, F401
from app.database.connection import Base, engine  # noqa: E402
from app.observability.logger import configure_logging  # noqa: E402

Base.metadata.create_all(bind=engine)

configure_logging()

app = FastAPI(
    title="AI Agent Quality Engineering Platform",
    version="0.1.0",
)

frontend_path = Path(__file__).parent / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=frontend_path / "static"),
    name="static",
)

app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
def frontend() -> FileResponse:
    return FileResponse(frontend_path / "templates" / "index.html")
