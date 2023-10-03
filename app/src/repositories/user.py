from src.models.user import User
from src.repositories.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
