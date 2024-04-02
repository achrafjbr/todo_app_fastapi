from pydantic import BaseModel
from typing import List


class NoteBase(BaseModel):
    note_title: str
    note_content: str
    note_date: str | None
    note_is_completed: bool = False


class NoteCreate(NoteBase):
    user_id: int


class Note(NoteCreate):  # inherits from NoteBase
        note_id: int

class UserBase(BaseModel):
    user_email: str

    class Config:
        from_attribute = True


class UserCreate(UserBase):
    user_password: str


class User(UserCreate):
    user_id: int
    notes: List[Note] = []

    class Config:
        from_attribute = True
