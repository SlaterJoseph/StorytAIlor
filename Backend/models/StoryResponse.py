from pydantic import BaseModel

class StoryResponse(BaseModel):
    content: str
    story_id = None
    user = None