from apis.v1.routes import users
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
