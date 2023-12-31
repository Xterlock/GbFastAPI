from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.connect import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, data: dict, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def delete_one(self, **filter_by):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(**filter_by)
            await session.commit()
            await session.execute(stmt)

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_one(self, **filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            res = res.scalar_one_or_none()
            return res

    async def find_all(self, **filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def edit_one(self, data: dict, **filter_by):
        async with async_session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(**filter_by).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
