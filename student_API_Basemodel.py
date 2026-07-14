from fastapi import FastAPI ,Query
from typing import Optional
from pydantic import BaseModel,Field 

app = FastAPI(
    title= "Student Management System ",
    description="Professional Student API",
    version="1.2.0"
    )
class Student(BaseModel):
    id: int = Field(gt=0)
    name: str =Field(min_length=3,max_length=70)
    age: int =Field(gt=18,le=60)
students = [
    {"id": 2,"name":"Noman","age": 23},
    {"id": 3,"name": "Ali","age": 24}
]
@app.get("/students")
def get_student():
    return students
@app.post("/students")
def create_Student(student:Student):
    students.append(student.model_dump())
    return{
        "message": "Student created successfully",
        "student": student
    }
@app.put("/students/{student_id}")
def update_Student(student_id:int ,student:Student):
    for index,old_student in enumerate(students):
        if old_student["id"] ==student_id:
            students[index] = student.model_dump()
            return {
                "message": "student updated successfully"
            }
    return{
        "message": "student not found"
    }
class Student_Update(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
@app.patch("/students/{student_id}")
def patch_student(student_id:int ,student:Student_Update):
    for old_student in students:
        if old_student["id"] ==student_id:
            if student.name is not None:
                old_student["name"]=student.name
            if student.age is not None:
                old_student["age"]=student.age
            return{
                "message": "student updated successfully"
            }
    return{
        "message":" student not found"
    }
@app.delete("/students/{student_id}")
def delete_student(student_id:int ):
    for student in students:
        if student["id"] ==student_id:
            students.remove(student)
            return{
                "message": "student deleted successfully"

            }
    return{
        "message": "student not found"
    }