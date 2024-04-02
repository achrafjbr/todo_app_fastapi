from fastapi import FastAPI, Depends, status, HTTPException
from .database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from . import schemas
from .enum_tags import Tags
from . import repository
from typing import List
from . import util
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# user_sign_up
@app.post('/user/signup', response_model=schemas.User,
          status_code=status.HTTP_201_CREATED, tags=[Tags.users])
async def sing_up(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if not util.check_email(user.user_email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email is not valid")
    if not util.check_password(user.user_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Password is not valid")
    response = await repository.sing_up(user=user, db=db)
    return response


@app.post('/notes', response_model=schemas.Note, tags=[Tags.notes])
async def add_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    response = await repository.add_note(db=db, note=note)
    return response


@app.get('/notes/{user_id}', response_model=List[schemas.NoteCreate], tags=[Tags.notes])
async def get_user_notes(user_id: int, db: Session = Depends(get_db)):
    return await repository.get_user_notes(db=db, user_id=user_id)
