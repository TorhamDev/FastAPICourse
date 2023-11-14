from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from oprations.users import UsersOpration
from schema._input import DeleteUserAccountInput, RegisterInput, UpdateUserProfileInput

router = APIRouter()


@router.post("/register")
async def register(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: RegisterInput = Body(),
):
    user = await UsersOpration(db_session).create(
        username=data.username,
        password=data.password,
    )
    return user


@router.post("/login")
async def login():
    ...


@router.get("/{username}/")
async def get_user_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    username: str,
):
    user_profile = await UsersOpration(db_session).get_user_by_username(username)

    return user_profile


@router.put("/")
async def user_update_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UpdateUserProfileInput = Body(),
):
    user = await UsersOpration(db_session).update_username(
        data.old_username, data.new_username
    )

    return user


@router.delete("/")
async def delete_user_account(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: DeleteUserAccountInput = Body(),
):
    await UsersOpration(db_session).user_delete_account(data.username, data.password)
