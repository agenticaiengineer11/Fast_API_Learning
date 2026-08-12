print("================Nested dependency===============")
from fastapi import FastAPI,Query,Depends,HTTPException

app = FastAPI()

def get_user():
    return{
        "id":1,
        "name":"Noman",
        "role":"admin"
    }

def require_admin(user = Depends(get_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin permission required"
        )
    return user

@app.get("/employees/{employee_id}")
def delete_employee(employee_id:int, user = Depends(require_admin)):
    return{
        "message":"employee deleted",
        "employee_id":employee_id,
        "deleted_by":user["name"]
    }
