from typing import List

from fastapi import APIRouter

from src.api.user import router as user_router
from src.api.product import router as product_router
from src.api.order import router as order_router

routers: List[APIRouter] = [
    user_router,
    product_router,
    order_router
]
