import hashlib
import secrets
from typing import Tuple

# Generate salt
def gen_salt() -> str:
    return secrets.token_urlsafe(20)

# Hash and salt password
def hash_password(password: str, salt: str) -> str:
    h = hashlib.sha256()
    h.update((password + salt).encode())
    return h.hexdigest()

def update_password_hashed_salted(password: str) -> Tuple[str, str]:
    salt = gen_salt()
    hashed_password = hash_password(password, salt)
    return hashed_password

# Test the function
hashed_password = update_password_hashed_salted('password')
print(f'Hashed Password: {hashed_password}')
