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
        "student" : student
    }