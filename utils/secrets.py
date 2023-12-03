from passlib.context import CryptContext

password_manager = CryptContext(schemes=["bcrypt"], deprecated="auto")
