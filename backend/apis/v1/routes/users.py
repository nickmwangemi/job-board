from db.repository.user import create_new_user
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.user import ShowUser, UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
