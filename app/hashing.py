from passlib.context import CryptContext


password_context = CryptContext(schemes='bcrypt', deprecated='auto')


class HashPass:

    @staticmethod
    def hash_password(password: str):
        return password_context.hash(password)

    @staticmethod
    def verify_password(hashed_password, password):
        return password_context.verify(password, hashed_password)
