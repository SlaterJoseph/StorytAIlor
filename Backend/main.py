from fastapi import FastAPI, HTTPException

from Backend.services import generate_chapter
from Backend.models import StoryResponse

app = FastAPI(title="StorytAIlor API")


@app.get("/")
async def root():
    return {"message": 'StorytAIlor API running'}

@app.post('/story/generate')
async def generate_story(prompt: str):
    try:
        story_content = generate_chapter(prompt)
        return StoryResponse(content=story_content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))