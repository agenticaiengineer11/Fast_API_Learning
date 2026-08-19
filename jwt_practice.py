import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "my_secret_key"
ALGORITHM= "HS256"

Payload = {
    "sub": "Noman",
    "role": "admin",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}
token = jwt.encode(
    Payload,
    SECRET_KEY,
    algorithm=ALGORITHM
)
print("JWT:")
print(token)

decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)

print("Decode: ")
print(decoded)