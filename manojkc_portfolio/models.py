# models.py
from sqlalchemy import Column, Integer, String, Text
from database import Base

class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    message = Column(Text)