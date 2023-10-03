from typing import Optional

from pydantic import BaseModel, Field


class ProductSchemaAdd(BaseModel):
    name: str = Field(max_length=64)
    description: str
    price: int = Field(gt=0)


class ProductSchema(ProductSchemaAdd):
    id: int


class ProductIdResponse(BaseModel):
    id: int


class UpdateProductParams(BaseModel):
    name: Optional[str] = Field(max_length=64, default=None)
    description: Optional[str] = None
    price: Optional[int] = Field(gt=0, default=None)

    async def get_params_dict(self):
        params = dict()
        if self.name and self.name != "":
            params["name"] = self.name
        if self.name:
            params["description"] = self.description
        if self.price:
            params["price"] = self.price
        return params
