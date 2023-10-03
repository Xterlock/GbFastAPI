from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.model import Base
from src.scheme.product import ProductSchema


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(length=64))
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()

    async def to_read_model(self) -> ProductSchema:
        return ProductSchema(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price
        )
