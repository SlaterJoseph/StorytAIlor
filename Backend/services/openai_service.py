from openai import OpenAI
from Backend.config import settings

client = OpenAI(
    api_key = settings.OPENAI_API_KEY,
)

def generate_chapter(prompt) -> client.responses:
    response = client.responses.create(
        model='gpt-5-nano-2025-08-07',
        instructions=settings.INSTRUCTIONS,
        input=prompt
    )

    return response


