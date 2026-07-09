"""
Shopping cart business logic
"""
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas

CART_EXPIRY_DAYS = 30
STALE_WARNING_DAYS = 7


def get_or_create_cart(session_id: str, db: Session, user_id: Optional[str] = None) -> models.Cart:
    """Get or create a cart. Logged-in users are matched by user_id first; if they don't
    have one yet but do have an anonymous cart for this browser session, that cart is
    claimed for them instead of creating a duplicate."""
    cart = None
    if user_id:
        cart = db.query(models.Cart).filter(models.Cart.user_id == user_id).first()

    if not cart:
        cart = db.query(models.Cart).filter(models.Cart.session_id == session_id).first()
        if cart and user_id and not cart.user_id:
            cart.user_id = user_id
            db.commit()
            db.refresh(cart)

    if not cart:
        cart = models.Cart(session_id=session_id, user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    return cart


def _serialize_cart(cart: models.Cart) -> dict:
    items = [{"product_id": item.product_id, "quantity": item.quantity} for item in cart.items]
    is_stale = False
    if cart.updated_at:
        is_stale = (datetime.utcnow() - cart.updated_at) > timedelta(days=STALE_WARNING_DAYS)
    return {"items": items, "updated_at": cart.updated_at, "is_stale": is_stale}


def get_cart(session_id: str, db: Session, user_id: Optional[str] = None):
    cart = get_or_create_cart(session_id, db, user_id)
    return _serialize_cart(cart)


def add_item_to_cart(session_id: str, cart_item: schemas.CartItemBase, db: Session, user_id: Optional[str] = None):
    product = db.query(models.Product).filter(models.Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < cart_item.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    cart = get_or_create_cart(session_id, db, user_id)
    existing_item = db.query(models.CartItem).filter(
        models.CartItem.cart_id == cart.id,
        models.CartItem.product_id == cart_item.product_id
    ).first()

    if existing_item:
        new_quantity = existing_item.quantity + cart_item.quantity
        if product.stock < new_quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock")
        existing_item.quantity = new_quantity
    else:
        db.add(models.CartItem(
            cart_id=cart.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity
        ))

    cart.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(cart)
    return {"message": "Item added to cart", "cart": _serialize_cart(cart)}


def update_cart_item(session_id: str, product_id: str, cart_item: schemas.CartItemBase, db: Session, user_id: Optional[str] = None):
    cart = get_or_create_cart(session_id, db, user_id)
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < cart_item.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    item = db.query(models.CartItem).filter(
        models.CartItem.cart_id == cart.id,
        models.CartItem.product_id == product_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not in cart")

    item.quantity = cart_item.quantity
    cart.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(cart)
    return {"message": "Cart updated", "cart": _serialize_cart(cart)}


def remove_item_from_cart(session_id: str, product_id: str, db: Session, user_id: Optional[str] = None):
    cart = get_or_create_cart(session_id, db, user_id)
    item = db.query(models.CartItem).filter(
        models.CartItem.cart_id == cart.id,
        models.CartItem.product_id == product_id
    ).first()
    if item:
        db.delete(item)
        cart.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(cart)
    return {"message": "Item removed from cart", "cart": _serialize_cart(cart)}


def clear_cart(session_id: str, db: Session, user_id: Optional[str] = None):
    cart = get_or_create_cart(session_id, db, user_id)
    db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id).delete()
    cart.updated_at = datetime.utcnow()
    db.commit()
    return {"message": "Cart cleared"}


def merge_cart_into_user(session_id: str, user_id: str, db: Session):
    """Called on login: folds an anonymous session cart into the authenticated user's cart."""
    session_cart = db.query(models.Cart).filter(models.Cart.session_id == session_id).first()
    if not session_cart:
        return
    if session_cart.user_id == user_id:
        return  # already this user's cart

    user_cart = db.query(models.Cart).filter(models.Cart.user_id == user_id).first()
    if not user_cart:
        # No existing user cart: simplest merge is just claiming the session cart.
        session_cart.user_id = user_id
        db.commit()
        return

    for item in session_cart.items:
        existing = db.query(models.CartItem).filter(
            models.CartItem.cart_id == user_cart.id,
            models.CartItem.product_id == item.product_id
        ).first()
        if existing:
            existing.quantity += item.quantity
        else:
            db.add(models.CartItem(
                cart_id=user_cart.id,
                product_id=item.product_id,
                quantity=item.quantity
            ))

    user_cart.updated_at = datetime.utcnow()
    db.delete(session_cart)
    db.commit()


def cleanup_expired_carts(db: Session):
    """Delete carts that haven't been touched in CART_EXPIRY_DAYS days."""
    cutoff = datetime.utcnow() - timedelta(days=CART_EXPIRY_DAYS)
    expired = db.query(models.Cart).filter(models.Cart.updated_at < cutoff).all()
    count = len(expired)
    for cart in expired:
        db.delete(cart)
    db.commit()
    return {"message": f"Cleaned up {count} expired cart(s)", "deleted_count": count}
