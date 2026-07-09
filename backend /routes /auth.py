"""
Authentication API routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from controllers import auth as auth_controller
from auth_utils import get_current_user

router = APIRouter(prefix="/api", tags=["auth"])


@router.post("/register", response_model=schemas.TokenResponse)
def register(data: schemas.UserRegister, db: Session = Depends(get_db)):
    """Register a new user and return an access token."""
    return auth_controller.register_user(data, db)


@router.post("/login", response_model=schemas.TokenResponse)
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    """Login and return an access token. Optionally merges an anonymous cart."""
    return auth_controller.login_user(data, db)


@router.post("/logout")
def logout():
    """JWT auth is stateless: logout is handled client-side by discarding the token."""
    return {"message": "Logged out"}


@router.get("/me", response_model=schemas.UserResponse)
def get_me(user: models.User = Depends(get_current_user)):
    """Return the currently authenticated user."""
    return user
