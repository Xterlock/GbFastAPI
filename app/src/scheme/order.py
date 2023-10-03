import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.models.status import OrderStatus
from src.scheme.product import ProductSchema
from src.scheme.user import UserSchema


class OrderSchemaAdd(BaseModel):
    status: OrderStatus = Field(default=OrderStatus.awaiting_payment)
    product_id: int = Field(gt=0)
    user_id: int = Field(gt=0)


class OrderSchema(BaseModel):
    id: int
    status: OrderStatus
    order_data: datetime.datetime
    product: ProductSchema
    user: UserSchema


class OrderUpdateParams(BaseModel):
    status: Optional[OrderStatus] = Field(default=None)
    product_id: Optional[int] = Field(gt=0, default=None)
    user_id: Optional[int] = Field(gt=0, default=None)

    async def get_params_dict(self):
        params = dict()
        if self.status:
            params["status"] = self.status
        if self.product_id:
            params["product_id"] = self.product_id
        if self.user_id:
            params["user_id"] = self.user_id
        return params
