from typing import List

from fastapi import APIRouter
from starlette import status

from src.api.dependencies import OrdersService, QueryID, FormID
from src.scheme.order import OrderSchemaAdd, OrderSchema, OrderUpdateParams
from src.scheme.response import IDResponse

router = APIRouter(prefix="/order", tags=["Order"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(order_add: OrderSchemaAdd, service: OrdersService):
    product_id = await service.add_order(order_add)
    return IDResponse(status=status.HTTP_201_CREATED, id=product_id)


@router.delete("", status_code=status.HTTP_202_ACCEPTED, response_model=IDResponse)
async def delete_order(order_id: FormID, service: OrdersService):
    await service.delete_one(order_id)
    return IDResponse(status=status.HTTP_202_ACCEPTED, id=order_id)


@router.get("", response_model=OrderSchema)
async def get_order(order_id: QueryID, service: OrdersService):
    order = await service.find_one(order_id)
    return order


@router.get("/all", response_model=List[OrderSchema])
async def get_all(service: OrdersService):
    order_list = await service.find_all()
    return order_list


@router.patch("", status_code=status.HTTP_202_ACCEPTED, response_model=OrderSchema)
async def update_product(params: OrderUpdateParams, order_id: QueryID, service: OrdersService):
    product_id = await service.update(params, order_id)
    product = await service.find_one(product_id)
    return product
