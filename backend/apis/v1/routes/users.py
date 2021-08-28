from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.user import create_new_user
from db.session import get_db
from schemas.user import UserCreate

router = APIRouter()


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
