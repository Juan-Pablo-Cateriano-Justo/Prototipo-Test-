"""
Authentication business logic
"""
import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas
from auth_utils import hash_password, verify_password, create_access_token
from controllers.cart import merge_cart_into_user


def register_user(data: schemas.UserRegister, db: Session):
    existing = db.query(models.User).filter(models.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(
        id=str(uuid.uuid4()),
        email=data.email,
        name=data.name,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer", "user": user}


def login_user(data: schemas.UserLogin, db: Session):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": user.id})

    # If the client sent along its anonymous session_id, fold that cart into the user's cart.
    if data.session_id:
        merge_cart_into_user(data.session_id, user.id, db)

    return {"access_token": token, "token_type": "bearer", "user": user}
