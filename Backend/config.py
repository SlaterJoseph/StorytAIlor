from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTIONS = os.getenv("INSTRUCTIONS")

    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY is not set")

    if not INSTRUCTIONS:
        raise Exception("INSTRUCTIONS is not set")

settings = Settings()
