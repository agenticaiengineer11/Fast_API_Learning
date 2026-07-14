print("==========Request Body======instead of query parameter======")
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Student API",
    description="Professional Student APi"
)
class Student(BaseModel):
    id : int
    name: str
    age : int
@app.post("/students")
def create_student(student: Student):
    return{
        "message": "Student created successfully",
        "student" : student.model_dump()                #model_dump() converts it into a normal Python dictionary.
    }

class Book(BaseModel):
    id : int
    title: str
    author: str
    price : int
@app.post("/books")
def create_book(book : Book):
    return {
        "message": "Book created successfully",
        "book": book
    }
class Employee(BaseModel):
    id : int
    name: str
    departement : str
    salary : int
@app.post("/employees")
def create_employee(employee:Employee):
    return{
        "message": "Employee Created successfully",
        "employee": employee
    }