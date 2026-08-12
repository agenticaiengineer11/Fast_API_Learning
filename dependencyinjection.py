print("=================Dependency Injection===========================")
from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters(page:int=1, limit:int = 5):
    return{
        "page": page,
        "limit": limit
    }
@app.get("/students")
def get_students(params = Depends(common_parameters)):
    return{

        "students":["Noman","Ali"],
        "pagination": params
    }

@app.get("/employees")
def get_employees(params = Depends(common_parameters)):
    return{
        "employees":["John","David"],
        "pagination":params
    }


print("==================Current user dependency================")
from fastapi import FastAPI, Depends

app = FastAPI()

def get_current_user():
    user={
        "id": 1,
        "name":"Muku",
        "role":"admin"
    }
    return user
@app.get("/profile")
def get_profile(user= Depends(get_current_user)):
    return{
        "message":"user retrived",
        "user": user
    }

@app.get("/employees")
def get_user(user=Depends(get_current_user)):
    return{
        "message":"Employee Data",
        "requested by": user
    }