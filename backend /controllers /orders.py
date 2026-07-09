"""
Order processing business logic
"""
import math
import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas

# Order status state machine (Reto 05)
VALID_TRANSITIONS = {
    "pending": {"processing", "cancelled"},
    "processing": {"successful", "failed", "cancelled"},
    "successful": set(),  # terminal
    "cancelled": set(),   # terminal
    "failed": set(),      # terminal
}
VALID_STATUSES = set(VALID_TRANSITIONS.keys())


def create_order(order_request: schemas.CreateOrderRequest, db: Session, user: models.User):
    if not order_request.cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order_items = []
    total = 0.0

    for cart_item in order_request.cart_items:
        product = db.query(models.Product).filter(
            models.Product.id == cart_item.product_id
        ).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {cart_item.product_id} not found")
        if product.stock < cart_item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for {product.name}")

        product.stock -= cart_item.quantity
        order_items.append(models.OrderItem(
            product_id=product.id,
            product_name=product.name,
            quantity=cart_item.quantity,
            price=product.price
        ))
        total += product.price * cart_item.quantity

    order = models.Order(
        id=str(uuid.uuid4()),
        total=round(total, 2),
        status="pending",
        user_id=user.id,
        items=order_items,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_all_orders(db: Session, user: models.User, page: int = 1, limit: int = 10):
    """Paginated order history, scoped to the current user (Retos 03 + 04)."""
    query = db.query(models.Order).filter(
        models.Order.user_id == user.id
    ).order_by(models.Order.created_at.desc())

    total = query.count()
    page = max(page, 1)
    limit = max(limit, 1)
    pages = math.ceil(total / limit) if total > 0 else 0

    if pages > 0 and page > pages:
        items = []
    else:
        items = query.offset((page - 1) * limit).limit(limit).all()

    return {"items": items, "total": total, "page": page, "limit": limit, "pages": pages}


def get_order_by_id(order_id: str, db: Session, user: models.User):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this order")
    return order


def update_order_status(order_id: str, new_status: str, db: Session, user: models.User):
    if new_status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail=f"Invalid status: {new_status}")

    order = get_order_by_id(order_id, db, user)
    allowed = VALID_TRANSITIONS.get(order.status, set())
    if new_status not in allowed:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot transition order from '{order.status}' to '{new_status}'"
        )

    order.status = new_status
    db.commit()
    db.refresh(order)
    return order
