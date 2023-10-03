from typing import List

from fastapi import APIRouter
from starlette import status

from src.api.dependencies import ProductsService, FormID, QueryID
from src.scheme.product import ProductSchemaAdd, ProductSchema, UpdateProductParams
from src.scheme.response import IDResponse

router = APIRouter(prefix="/product", tags=["Product"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=IDResponse)
async def create_product(product_add: ProductSchemaAdd, service: ProductsService):
    product_id = await service.add_product(product_add)
    return IDResponse(status=status.HTTP_201_CREATED, id=product_id)


@router.delete("", status_code=status.HTTP_202_ACCEPTED, response_model=IDResponse)
async def delete_product(product_id: FormID, service: ProductsService):
    await service.delete_one(product_id)
    return IDResponse(status=status.HTTP_202_ACCEPTED, id=product_id)


@router.get("", response_model=ProductSchema)
async def get_product(product_id: QueryID, service: ProductsService):
    product = await service.find_one(product_id)
    return product


@router.get("/all", response_model=List[ProductSchema])
async def get_all(service: ProductsService):
    product_list = await service.find_all()
    return product_list


@router.patch("", status_code=status.HTTP_202_ACCEPTED, response_model=ProductSchema)
async def update_product(params: UpdateProductParams, product_id: int, service: ProductsService):
    product_id = await service.update(params, product_id)
    product = await service.find_one(product_id)
    return product
