"""
Order API routes
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from controllers import orders as order_controller
from auth_utils import get_current_user

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.post("", response_model=schemas.OrderResponse)
def create_order(
    order: schemas.CreateOrderRequest,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """Create an order from the cart. Requires authentication (Reto 03)."""
    return order_controller.create_order(order, db, user)


@router.get("", response_model=schemas.OrderListResponse)
def get_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """Paginated order history for the current user (Retos 03 + 04)."""
    return order_controller.get_all_orders(db, user, page, limit)


@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: str, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """Get a single order (only if it belongs to the current user)."""
    return order_controller.get_order_by_id(order_id, db, user)


@router.patch("/{order_id}/status", response_model=schemas.OrderResponse)
def update_order_status(
    order_id: str,
    status_update: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """Update order status with valid-transition enforcement (Reto 05)."""
    return order_controller.update_order_status(order_id, status_update.status, db, user)
