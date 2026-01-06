from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(__file__).parent.parent/'.env'
load_dotenv(dotenv_path)

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTIONS = os.getenv("INSTRUCTIONS")
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_MINUTES = os.getenv("JWT_ACCESS_TOKEN_MINUTES")

    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY is not set")

    if not INSTRUCTIONS:
        raise Exception("INSTRUCTIONS is not set")

    if not DATABASE_URL:
        raise Exception("DATABASE_URL is not set")

    if not JWT_SECRET_KEY:
        raise Exception("JWT_SECRET_KEY is not set")

    if not JWT_ACCESS_TOKEN_MINUTES:
        raise Exception("JWT_ACCESS_TOKEN_MINUTES is not set")

settings = Settings()
