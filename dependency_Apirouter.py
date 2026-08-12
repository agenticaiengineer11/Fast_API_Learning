from fastapi import FastAPI, Depends, APIRouter

app = FastAPI()


def get_current_user():
    return {
        "id": 1,
        "name": "Noman",
        "role": "admin"
    }


employee_router = APIRouter(
    prefix="/employee",
    tags=["Employees"],
    dependencies=[Depends(get_current_user)]
)


@employee_router.get("/")
def get_employee():
    return {
        "employees": ["Noman", "Ali"]
    }


@employee_router.post("/")
def create_employee():
    return {
        "message": "Employee created"
    }


@employee_router.delete("/{employee_id}")
def delete_employee(employee_id: int):
    return {
        "message": "Employee deleted",
        "employee_id": employee_id
    }


app.include_router(employee_router)