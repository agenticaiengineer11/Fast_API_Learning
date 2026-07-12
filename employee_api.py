from fastapi import FastAPI,Query
from typing import Annotated
app = FastAPI(
    title="Employee Management System",
    description="Professional CRUD API",
    version="1.0.0"
)

employees = [
    {"id":1 , "name":"John","salary":50000},
    {"id":2, "name": "Bajwa", "salary": 60000}
]
@app.get("/employees")
def get_employee():
    return employees
@app.get("/employees/search")
def search_employees(
    name: Annotated[str , Query(min_length=3, max_length=30)],
    salary:Annotated[ int , Query(gt=20000, le=500000)]
):
    return {
        "name": name,
        "salary": salary
    }
@app.get("/employees/{employee_id}")
def get_employee(employee_id:int):
    for employee in employees:
        if employee["id"]==employee_id:
            return employee
    return{
        "message": "employee not found"
    }
@app.post("/employees")
def create_employee(employee_id:int,name:str , salary:int):
    new_employee ={
        "id" : employee_id,
        "name" : name,
        "salary" : salary,
    }
    employees.append(new_employee)
    return {
        "message": "Employee added successfully",
        "employee": new_employee
    }
@app.put("/employees/{employee_id}")
def update_employee(employee_id:int,name:str,age:int):
    for employee in employees:
        if employee["id"]== employee_id:
            employee["name"]= name
            employee["age"]= age
            return{
                "message": "Employee updated successfully",
                "employee": employee
            }
    return {
        "message": "employee not found"
    }
@app.patch("/employees/{employee_id}")
def patch_employee(employee_id:int, salary:int):
    for employee in employees:
        if employee["id"]==employee_id:
            employee["salary"]=salary
            return{
                "message": "salary patched successfully"
            }
    return{
        "message": "employee not found"
    }
@app.delete("/employee/{employee_id}")
def delete_employee(employee_id:int):
    for employee in employees:
        if employee["id"]== employee_id:
            employees.remove(employee)
            return {
                "message": "employee deleted successfully"
            }
    return {
        "message ": "employee not found"
    }