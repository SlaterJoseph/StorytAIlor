from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from schema.User import UserLogin, UserLoginResponse
from db.database import get_db
from services.account import authenticate_user
from security.jwt import create_access_token
from config import Settings

router = APIRouter()

@router.post("/login", response_model=UserLoginResponse)
async def login(login_payload: UserLogin, db: Session = Depends(get_db)):
    username_or_password = login_payload.username_or_email
    password = login_payload.password

    try:
        user = authenticate_user(db, username_or_password, password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=Settings.JWT_ACCESS_TOKEN_MINUTES))

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }

