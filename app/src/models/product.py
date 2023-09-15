from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.model import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(length=64))
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
