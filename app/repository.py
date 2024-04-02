from sqlalchemy.orm import Session

from . import schemas
from . import models


async def sing_in(db: Session, user: schemas.UserCreate):  # i'm gonna do implementation later
    pass


async def sing_up(db: Session, user: schemas.UserCreate):  # i'm gonna do implementation later
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def add_note(db: Session, note: schemas.NoteCreate):
    note_db = models.Note(**note.model_dump())
    db.add(note_db)
    db.commit()
    db.refresh(note_db)
    return note_db


async def delete_note(db: Session, note_id: int):
    note = db.query(models.Note) \
        .filter(models.Note.note_id == note_id) \
        .first()
    db.delete(note)


async def get_user_notes(db: Session, user_id: int):
    return db.query(models.Note) \
        .filter(models.Note.user_id == user_id) \
        .all()
