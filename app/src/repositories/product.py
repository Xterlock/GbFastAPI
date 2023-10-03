from src.models.product import Product
from src.repositories.repository import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    model = Product
