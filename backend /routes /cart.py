"""
Shopping cart API routes
"""
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from controllers import cart as cart_controller
from auth_utils import get_current_user_optional

router = APIRouter(prefix="/api/cart", tags=["cart"])
# Separate router because the cleanup endpoint lives under the plural /api/carts path.
cleanup_router = APIRouter(prefix="/api/carts", tags=["cart"])


def _uid(user: Optional[models.User]) -> Optional[str]:
    return user.id if user else None


@router.get("/{session_id}", response_model=schemas.CartResponse)
def get_cart(session_id: str, db: Session = Depends(get_db), user=Depends(get_current_user_optional)):
    """Get cart for a session. If logged in, resolves to the user's cart."""
    return cart_controller.get_cart(session_id, db, _uid(user))


@router.post("/{session_id}/items")
def add_to_cart(
    session_id: str,
    cart_item: schemas.CartItemBase,
    db: Session = Depends(get_db),
    user=Depends(get_current_user_optional)
):
    return cart_controller.add_item_to_cart(session_id, cart_item, db, _uid(user))


@router.put("/{session_id}/items/{product_id}")
def update_cart_item(
    session_id: str,
    product_id: str,
    cart_item: schemas.CartItemBase,
    db: Session = Depends(get_db),
    user=Depends(get_current_user_optional)
):
    return cart_controller.update_cart_item(session_id, product_id, cart_item, db, _uid(user))


@router.delete("/{session_id}/items/{product_id}")
def remove_from_cart(
    session_id: str,
    product_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user_optional)
):
    return cart_controller.remove_item_from_cart(session_id, product_id, db, _uid(user))


@router.delete("/{session_id}")
def clear_cart(session_id: str, db: Session = Depends(get_db), user=Depends(get_current_user_optional)):
    return cart_controller.clear_cart(session_id, db, _uid(user))


@cleanup_router.delete("/cleanup")
def cleanup_expired_carts(db: Session = Depends(get_db)):
    """Remove carts inactive for more than 30 days (Reto 07)."""
    return cart_controller.cleanup_expired_carts(db)
