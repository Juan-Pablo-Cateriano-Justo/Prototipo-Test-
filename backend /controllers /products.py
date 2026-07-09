"""
Product business logic
"""
import math
import uuid
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, asc, desc
from fastapi import HTTPException
import models
import schemas

SORT_COLUMNS = {
    "price": lambda: models.Product.price,
    "name": lambda: models.Product.name,
    "stock": lambda: models.Product.stock,
}


def get_products(
    db: Session,
    page: int = 1,
    limit: int = 10,
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = None,
    order: str = "asc",
):
    """List products with optional search/filter/sort, combined with pagination."""
    query = db.query(models.Product)

    if search:
        like = f"%{search}%"
        query = query.filter(
            or_(models.Product.name.ilike(like), models.Product.description.ilike(like))
        )

    if min_price is not None:
        query = query.filter(models.Product.price >= min_price)
    if max_price is not None:
        query = query.filter(models.Product.price <= max_price)

    sort_column = SORT_COLUMNS.get(sort_by, SORT_COLUMNS["name"])()
    query = query.order_by(desc(sort_column) if order == "desc" else asc(sort_column))

    total = query.count()
    page = max(page, 1)
    limit = max(limit, 1)
    pages = math.ceil(total / limit) if total > 0 else 0

    if pages > 0 and page > pages:
        items = []
    else:
        items = query.offset((page - 1) * limit).limit(limit).all()

    return {"items": items, "total": total, "page": page, "limit": limit, "pages": pages}


def get_product_by_id(product_id: str, db: Session):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def create_product(product_data: schemas.ProductCreate, db: Session):
    db_product = models.Product(id=str(uuid.uuid4()), **product_data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def init_sample_products(db: Session):
    """Initialize database with sample products if empty"""
    count = db.query(models.Product).count()
    if count > 0:
        return
    sample_products = [
        models.Product(
            id=str(uuid.uuid4()),
            name="Wireless Headphones",
            description="High-quality wireless headphones with noise cancellation",
            price=99.99,
            stock=50,
            image_url="https://i.imgur.com/ZANVnHE.jpg"
        ),
        models.Product(
            id=str(uuid.uuid4()),
            name="Smart Watch",
            description="Fitness tracker with heart rate monitor",
            price=199.99,
            stock=30,
            image_url="https://i.imgur.com/mp3rUty.jpg"
        ),
        models.Product(
            id=str(uuid.uuid4()),
            name="Laptop Backpack",
            description="Water resistant laptop backpack with USB charging port",
            price=49.99,
            stock=100,
            image_url="https://i.imgur.com/9DqEOV5.jpg"
        ),
        models.Product(
            id=str(uuid.uuid4()),
            name="Running Shoes",
            description="Comfortable running shoes with excellent cushioning",
            price=89.99,
            stock=75,
            image_url="https://i.imgur.com/tXeOYWE.jpg"
        ),
        models.Product(
            id=str(uuid.uuid4()),
            name="Mechanical Keyboard",
            description="RGB mechanical keyboard with blue switches",
            price=129.99,
            stock=40,
            image_url="https://i.imgur.com/R3iobJA.jpg"
        ),
        models.Product(
            id=str(uuid.uuid4()),
            name="Wireless Mouse",
            description="Ergonomic wireless mouse with precision tracking",
            price=29.99,
            stock=120,
            image_url="https://i.imgur.com/w3Y8NwQ.jpg"
        ),
    ]
    db.add_all(sample_products)
    db.commit()
