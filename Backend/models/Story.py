from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from db.base import Base

class Story(Base):
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(ForeignKey("users.id"))
    user = relationship("User", back_populates="stories")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
