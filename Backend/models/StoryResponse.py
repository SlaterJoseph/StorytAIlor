from pydantic import BaseModel
from typing import List


class StoryResponse(BaseModel):
    responses: List[str]  # Changed from 'chapters' to 'responses' to match frontend

    def __init__(self, chapter_1=None, **data):
        if chapter_1 is not None:
            # If chapter_1 is provided, create responses list
            data['responses'] = [chapter_1]
        super().__init__(**data)

    def __str__(self) -> str:
        # Provide a concise, human-friendly summary of the response
        try:
            total = len(self.responses) if self.responses is not None else 0
            previews = []
            for i, ch in enumerate(self.responses or [], start=1):
                text = ("" if ch is None else str(ch)).strip().replace("\n", " ")
                preview = text if len(text) <= 60 else text[:57] + "..."
                previews.append(f"{i}: {len(ch or '')} chars - \"{preview}\"")
            previews_str = "; ".join(previews)
            return f"StoryResponse({total} responses) [{previews_str}]"
        except Exception:
            # Fallback to BaseModel's string if anything unexpected happens
            return super().__str__()

