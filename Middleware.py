print("======================First Middleware========================")
from fastapi import FastAPI, middleware,Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("Response received")

    response= await call_next(request)

    print("Response Generated")

    return response
@app.get("/")
def home():
    return{
        "message": "Welcome to fastapi"
    }
