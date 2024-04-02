from sqlalchemy import Column, \
    Integer, ForeignKey, TEXT, Boolean, Date , VARCHAR
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_email = Column(VARCHAR(255), index=True)
    user_password = Column(VARCHAR(255))
    notes = relationship("Note", back_populates="user")


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    note_title = Column(VARCHAR(400), unique=True, index=True)
    note_content = Column(TEXT, nullable=True)
    note_is_completed = Column(Boolean, default=False)
    note_date = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="notes")
