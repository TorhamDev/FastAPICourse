from .engine import Base, engine
from .models import User

__all__ = [
    "Base",
    "User",
]

Base.metadata.create_all(bind=engine)
