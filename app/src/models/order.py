import datetime
import enum

from sqlalchemy import ForeignKey, DATETIME, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.testing.pickleable import User

from db.model import Base
from models.product import Product


class OrderStatus(enum.StrEnum):
    ready = "Готов"
    issued = "Выдан"
    paid = "Оплачен"
    awaiting_payment = "Ожидает оплаты"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    order_date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    status: Mapped[str] = mapped_column(Enum(OrderStatus))

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped[Product] = relationship(lazy="joined")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(lazy="joined")
