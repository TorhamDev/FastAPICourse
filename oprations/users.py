import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from exceptions import UserAlreadyExists, UserNotFound
from schema.output import RegisterOutput
from utils.secrets import password_manager


class UsersOpration:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username: str, password: str) -> RegisterOutput:
        user_pwd = password_manager.hash(password)
        user = User(password=user_pwd, username=username)

        async with self.db_session as session:
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                raise UserAlreadyExists

        return RegisterOutput(username=user.username, id=user.id)

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)

        async with self.db_session as session:
            user_data = await session.scalar(query)

            if user_data is None:
                raise UserNotFound("/get")

            return user_data

    async def update_username(self, old_username: str, new_username: str) -> User:
        query = sa.select(User).where(User.username == old_username)
        update_query = (
            sa.update(User)
            .where(User.username == old_username)
            .values(username=new_username)
        )
        async with self.db_session as session:
            user_data = await session.scalar(query)

            if user_data is None:
                raise UserNotFound("/update")

            await session.execute(update_query)
            await session.commit()

            user_data.username = new_username
            return user_data

    async def user_delete_account(self, username: str, password: str) -> None:
        delete_query = sa.delete(User).where(username == username, password == password)  # type: ignore

        async with self.db_session as session:
            await session.execute(delete_query)
            await session.commit()
