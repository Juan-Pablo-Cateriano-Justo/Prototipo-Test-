"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


# ---------- Product Schemas ----------
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: str

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    items: List[Product]
    total: int
    page: int
    limit: int
    pages: int


# ---------- Cart Schemas ----------
class CartItemBase(BaseModel):
    product_id: str
    quantity: int


class CartItem(CartItemBase):
    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    items: List[CartItem]
    updated_at: Optional[datetime] = None
    is_stale: bool = False


# ---------- Order Schemas ----------
class OrderItemBase(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    price: float


class OrderItem(OrderItemBase):
    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: str
    items: List[OrderItem]
    total: float
    status: str
    created_at: datetime
    user_id: Optional[str] = None

    class Config:
        from_attributes = True


class OrderListResponse(BaseModel):
    items: List[OrderResponse]
    total: int
    page: int
    limit: int
    pages: int


class CreateOrderRequest(BaseModel):
    cart_items: List[CartItem]


class OrderStatusUpdate(BaseModel):
    status: str


# ---------- Auth / User Schemas ----------
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    session_id: Optional[str] = None  # anonymous cart session to merge on login


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
