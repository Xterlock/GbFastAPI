from src.models.order import Order
from src.repositories.repository import SQLAlchemyRepository


class OrderRepository(SQLAlchemyRepository):
    model = Order
