from fastapi import FastAPI,Depends , HTTPException

import jwt 
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

SECRET_KEY = "my_secret_key"

ALGORITHM = "HS256"

oauth2_Schema = OAuth2PasswordBearer(tokenUrl="Login")

users = {
    "Noman":{
        "username": "Noman",
        "password": "12345",
        "role":"admin",

    }
}
def create_access_token(data:str):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    payload["exp"] = expire

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = users.get(form_data.username)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if user["password"] != form_data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/profile")
def get_profile(
    token: str = Depends(oauth2_Schema)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")

        return {
            "message": "Authenticated successfully",
            "username": username,
            "role": role
        }

    except jwt.ExpiredSignatureError:

        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )