from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from db.base import Base

class Chapter(Base):
    __tablename__ = "chapter"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True)
    associated_story_id = Column(ForeignKey("story.id"))
    story = relationship("Story", back_populates="chapters")
    associated_uder_id = Column(ForeignKey("users.id"))
    writer = relationship("User", back_populates="chapters")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    content = Column(String)