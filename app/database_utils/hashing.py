from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    return context.hash(password)
