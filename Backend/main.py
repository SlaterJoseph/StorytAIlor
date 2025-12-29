from fastapi import FastAPI, HTTPException, Depends
from contextlib import contextmanager, asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
import logging
from sqlalchemy.orm import Session

from services.openai_service import generate_chapter, connect_to_openai
from models.StoryResponse import StoryResponse
from models.Message import Message
from db.database import create_db_and_tables, get_db

logger = logging.getLogger("uvicorn")
client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global client
    client = connect_to_openai()
    logger.info(f"Connecting to OpenAI service")

    create_db_and_tables()
    logger.info(f"Database Connected")

    yield
    logger.info(f"Shutting Down")

app = FastAPI(title="StorytAIlor API", lifespan=lifespan)
debug = True

# CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    if debug:
        logger.info("Root Endpoint Hit")

    return {"message": 'StorytAIlor API running'}

@app.post('/api/message')
async def generate_story(message: Message):
    logger.debug("Recieving Message")
    try:
        chapter = generate_chapter(message.message, client)
        logger.info(f"Chapter Generated")
        response = StoryResponse(chapter_1=chapter)
        logger.info(f"Sending Response")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @app.post('/api/pdf')
# async def generate_pdf():


# @app.get('/api/test')
# async def generate_story():
#     logger.debug("Recieving Message")
#     try:
#         chapter = generate_chapter(message.message)
#         response = StoryResponse(chapter_1=chapter)
#         logger.debug("Sending Response")
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
