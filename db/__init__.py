from db import db, User
from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

db.create_all()

admin = User(username = "admin", email = "admin@jacobs-university.de", passwd = encrypt_password("admin"), items = ["apples", "flour", "sugar"])

db.session.add(admin)

db.session.commit()