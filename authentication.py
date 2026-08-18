from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username == "Noman" and form_data.password == "12345":
        return {
            "access_token": "abc123",
            "token_type": "bearer"
        }

    return {
        "message": "Invalid username or password"
    }


@app.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Authenticated request",
        "token": token
    }