from fastapi import FastAPI
from pydantic import Field , BaseModel
from typing import Optional
app = FastAPI(
    title="Employee Management System ",
    description="Professional fast employee management system",
    version= "2.0.1"
)

employees = [
    {
        "id":1,
        "name":"Noman",
        "department":"finance",
        "salary": 60000
    },
    {
        "id":2,
        "name": "Mukurram",
        "department": "Marketing",
        "salary": 67000
    }
]
class EmployeeCreate(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3,max_length=20)
    department: str = Field(min_length=5,max_length=20)
    salary: int = Field(gt=25000,le=500000)
class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(default=None,min_length=3,max_length=50)
    department: Optional[str] = Field(default=None,min_length=3,max_length=50)
    salary: Optional[int] = Field(default=None, ge=25000, le=500000)
class EmployeeResponse(BaseModel):
    id:int
    name:str
    department: str
@app.get("/employees",response_model  = list[EmployeeResponse])
def get_employees():
    return employees
@app.get("/employees/{employee_id}",response_model=EmployeeResponse)
def get_all(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
        else:
            return {
                "message": "employee not found"
            }
@app.post("/employees",response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate):
    employees.append(employee.model_dump())
    return employee

@app.patch("/employees/{employee_id}",response_model=EmployeeResponse)
def Patch_employee(employee_id:int,employee:EmployeeUpdate):
    for old_employee in employees:
        if old_employee["id"] == employee_id:
            if employee.name is not None:
                old_employee["name"] = employee.name
            if employee.department is not None:
                old_employee["department"] = employee.department
            if employee.salary is not None:
                old_employee["salary"] = employee.salary
            
            return old_employee
    return{
        "message": "Employee not found"
    }
@app.put("/employees/{employee_id}",response_model=EmployeeResponse)
def Update_employee(employee_id:int , employee:EmployeeCreate):
    for index, old_employee in enumerate(employees):
        if old_employee["id"] == employee_id:
            employee_data = employee.model_dump()
            employee_data["id"] = employee_id
            employees[index] = employee_data
            
            return employee_data
    return {
        "message": "Employee not found"
    }
@app.delete("/employees/{employee_id}",response_model=EmployeeResponse)
def delete_employee(employee_id:int):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)

            return employee
    return {
        "message": "employee not found"
    }
