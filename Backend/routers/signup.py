from datetime import timedelta

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from config import Settings
from db.database import get_db
from schema.User import UserCreate, UserLoginResponse
from services.account import create_user
from security.jwt import create_access_token

router = APIRouter()

@router.post("/signup", response_model=UserLoginResponse)
async def signup(create_payload: UserCreate, db: Session = Depends(get_db)):
    username = create_payload.username
    email = create_payload.email
    password = create_payload.password

    try:
        user = create_user(db, username, email.__str__(), password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

    token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=Settings.JWT_ACCESS_TOKEN_MINUTES))

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }