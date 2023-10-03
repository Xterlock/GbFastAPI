from typing import List

from fastapi import HTTPException
from loguru import logger
from starlette import status

from src.models.order import Order
from src.repositories.order import OrderRepository
from src.scheme.order import OrderSchemaAdd, OrderUpdateParams


class OrderService:
    repository = OrderRepository()
    ex = HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def add_order(self, order_add: OrderSchemaAdd):
        try:
            order_id = await self.repository.add_one(order_add.model_dump())
            return order_id
        except Exception as ex:
            logger.warning(f"Не получилось добавить заказ: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_one(self, oder_id: int):
        try:
            order_model: Order = await self.repository.find_one(id=oder_id)
            order = await order_model.to_read_model()
            return order
        except Exception as ex:
            logger.warning(f"Не получилось получить заказ: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_all(self):
        try:
            order_model_list: List[Order] = await self.repository.find_all()
            return [await order_model.to_read_model() for order_model in order_model_list]
        except Exception as ex:
            logger.warning(f"Не получилось получить список заказов: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def delete_one(self, order_id: int):
        try:
            await self.repository.delete_one(id=order_id)
        except Exception as ex:
            logger.warning(f"Не получилось получить удалить заказ: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def update(self, params: OrderUpdateParams, order_id: int):
        try:
            data = await params.get_params_dict()
            product_id = await self.repository.edit_one(data, id=order_id)
            return product_id
        except Exception as ex:
            logger.warning(f"Не получилось получить обновить заказ: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")
