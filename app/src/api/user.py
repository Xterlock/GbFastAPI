from typing import List

from fastapi import APIRouter
from starlette import status

from src.api.dependencies import UsersService, FormID, QueryID
from src.scheme.response import IDResponse
from src.scheme.user import (
    UserSchemaAdd,
    UserSchema,
    UpdateUserParams,
)

router = APIRouter(prefix="/users", tags=["User"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=IDResponse)
async def create_user(user: UserSchemaAdd, service: UsersService):
    user_id = await service.add_user(user)
    return IDResponse(status=status.HTTP_201_CREATED, id=user_id)


@router.delete("", status_code=status.HTTP_202_ACCEPTED, response_model=IDResponse)
async def delete_user(user_id: FormID, service: UsersService):
    await service.delete_user(user_id)
    return IDResponse(status=status.HTTP_202_ACCEPTED, id=user_id)


@router.patch("", status_code=status.HTTP_202_ACCEPTED, response_model=UserSchema)
async def update_user(update_params: UpdateUserParams, user_id: QueryID, service: UsersService):
    user_id = await service.update_user_model(update_params, user_id)
    user = await service.find_one(user_id)
    return user


@router.get("", response_model=UserSchema)
async def get_user(user_id: QueryID, service: UsersService):
    user = await service.find_one(user_id)
    return user


@router.get("/all", response_model=List[UserSchema])
async def get_all(service: UsersService):
    users = await service.find_all()
    return users
