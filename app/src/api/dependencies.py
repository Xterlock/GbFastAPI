from typing import Annotated

from fastapi import Depends, Form, Query

from src.services.order import OrderService
from src.services.product import ProductService
from src.services.user import UserService


def user_service():
    return UserService()


def product_service():
    return ProductService()


def order_service():
    return OrderService()


UsersService = Annotated[UserService, Depends(user_service)]
ProductsService = Annotated[ProductService, Depends(product_service)]
OrdersService = Annotated[OrderService, Depends(order_service)]
FormID = Annotated[int, Form(gt=0)]
QueryID = Annotated[int, Query(gt=0)]
