import datetime
import enum

from sqlalchemy import ForeignKey, DATETIME, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.model import Base
from src.models.product import Product
from src.models.status import OrderStatus
from src.models.user import User
from src.scheme.order import OrderSchema


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    order_date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    status: Mapped[str] = mapped_column(Enum(OrderStatus))

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped[Product] = relationship(lazy="joined")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(lazy="joined")

    async def to_read_model(self) -> OrderSchema:
        user = await self.user.to_read_model()
        product = await self.product.to_read_model()
        return OrderSchema(
            id=self.id,
            order_data=self.order_date,
            status=self.status,
            product=product,
            user=user
        )
