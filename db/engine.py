from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

SQLALCHAMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
