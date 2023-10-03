from typing import List

from fastapi import HTTPException
from loguru import logger
from starlette import status

from src.models.product import Product
from src.repositories.product import ProductRepository
from src.scheme.product import ProductSchemaAdd, UpdateProductParams


class ProductService:
    repository = ProductRepository()

    async def add_product(self, product: ProductSchemaAdd) -> int:
        try:
            product_id = await self.repository.add_one(product.model_dump())
            return product_id
        except Exception as ex:
            logger.warning(f"Не получилось добавить товар: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def delete_one(self, product_id: int):
        try:
            await self.repository.delete_one(id=product_id)
        except Exception as ex:
            logger.warning(f"Не получилось удалить товар: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_one(self, product_id: int):
        try:
            product_model: Product = await self.repository.find_one(id=product_id)
            product = await product_model.to_read_model()
            return product
        except Exception as ex:
            logger.warning(f"Не получилось получить продукт с id={product_id}: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_all(self):
        try:
            product_model_list: List[Product] = await self.repository.find_all()
            return [await product_model.to_read_model() for product_model in product_model_list]
        except Exception as ex:
            logger.warning(f"Не получилось получить cписок продуктов: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def update(self, params: UpdateProductParams, product_id: int):
        try:
            data = await params.get_params_dict()
            product_id = await self.repository.edit_one(data, id=product_id)
            return product_id
        except Exception as ex:
            logger.warning(f"Не получилось получить обновить продукт: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")
