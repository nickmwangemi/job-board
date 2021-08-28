from db.repository.job import create_new_job
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.job import JobCreate, ShowJob
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/jobs/create", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    job = create_new_job(job=job, db=db, owner_id=1)
    return job
