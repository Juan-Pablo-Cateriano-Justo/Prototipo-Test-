"""
Product API routes
"""
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
import schemas
from controllers import products as product_controller

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=schemas.ProductListResponse)
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = None,
    order: str = "asc",
    db: Session = Depends(get_db),
):
    """List products with pagination (Reto 04) and search/filter/sort (Reto 06)."""
    return product_controller.get_products(
        db, page=page, limit=limit, search=search,
        min_price=min_price, max_price=max_price, sort_by=sort_by, order=order,
    )


@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: str, db: Session = Depends(get_db)):
    """Get a single product by ID"""
    return product_controller.get_product_by_id(product_id, db)


@router.post("", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Create a new product (for admin/testing)"""
    return product_controller.create_product(product, db)
