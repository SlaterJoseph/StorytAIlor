from openai import OpenAI
from config import settings
import logging

logger = logging.getLogger("uvicorn")

def connect_to_openai() -> OpenAI:
    client = OpenAI(
        api_key = settings.OPENAI_API_KEY,
    )
    return client

def generate_chapter(prompt, client) -> OpenAI.responses:
    logger.info(f"Generating chapter {prompt}")

    try:
        response = client.responses.create(
            model='gpt-5-nano-2025-08-07',
            instructions=settings.INSTRUCTIONS,
            input=prompt
        )
    except Exception as e:
        logger.error(f"Error generating chapter {prompt}: {e}")

    # logger.info(f"Chapter {prompt} response: {response.output[1].content[0].text}")
    logger.info(f"Chapter Parsed")
    return response.output[1].content[0].text
