print("===========Response Model=============")
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Usercreate(BaseModel):
    username : str
    email : str
    password : str
class UserResponse(BaseModel):
    username :str
    email : str
@app.post("/users",response_model=UserResponse)
def create_user(user:Usercreate):
    return user