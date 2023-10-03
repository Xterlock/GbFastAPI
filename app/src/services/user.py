from typing import List

from loguru import logger
from fastapi import HTTPException
from starlette import status

from src.models.user import User
from src.repositories.user import UserRepository
from src.scheme.user import UserSchemaAdd, UpdateUserParams


class UserService:
    repository = UserRepository()

    async def add_user(self, user: UserSchemaAdd) -> int:
        try:
            user = await self.repository.add_one(user.model_dump())
            return user
        except Exception as ex:
            logger.warning(f"Не получилось добавить пользователя: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def delete_user(self, user_id: int):
        try:
            await self.repository.delete_one(id=user_id)
        except Exception as ex:
            logger.warning(f"Не получилось удалить пользователя: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_one(self, user_id: int):
        try:
            user_model: User = await self.repository.find_one(id=user_id)
            return await user_model.to_read_model()
        except Exception as ex:
            logger.warning(f"Не получилось получить пользователя с id={user_id}: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def find_all(self):
        try:
            user_model_list: List[User] = await self.repository.find_all()
            return [await user_model.to_read_model() for user_model in user_model_list]
        except Exception as ex:
            logger.warning(f"Не получилось получить список пользователей: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")

    async def update_user_model(self, update_params: UpdateUserParams, user_id: int):
        try:
            params = await update_params.get_params_dict()
            user_id = await self.repository.edit_one(params, id=user_id)
            return user_id
        except Exception as ex:
            logger.warning(f"Не получилось обновить модель пользователя: {ex}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="BAD REQUEST")
