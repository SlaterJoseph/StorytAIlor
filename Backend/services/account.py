from sqlalchemy.orm import Session
from sqlalchemy import or_

from models.User import User
from security.hashing import verify_password, get_password_hash

def authenticate_user(db: Session, username_or_email: str, password: str):
    user = db.query(User).filter(
        or_(
            User.username == username_or_email,
            User.email == username_or_email
        )
    ).first()

    if not user or not verify_password(password, user.hashed_password):
        raise ValueError("Invalid Credentials")

    return user


def create_user(db: Session, username: str, password: str, email: str):
    existing_user = db.query(User).filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        raise ValueError("User already exists")

    hashed_password = get_password_hash(password)
    user = User(username=username, hashed_password=hashed_password, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
