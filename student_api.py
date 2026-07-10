from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students = [
    {"id": 1, "name": "Noman", "age": 22},
    {"id": 2, "name": "Ali", "age": 24}
]

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}
@app.post("/students")
def create_student(id:int,name:str,age:int):
    new_Student = {
        "id":id,
        "name":name,
        "age":age
    }
    students.append(new_Student)
    return {
        "message": "Student added successfully",
        "student": new_Student
    }
@app.put("/students/{student_id}")
def update_student(student_id: int , name: str,age: int):
    for student in students:
        if student["id"]== student_id:
            
            student["name"]=name
            student["age"]=age

            return {
                "message": "student updated",
                "student": student
            }
    return {
            "message": "student not found"
        }

@app.patch("/students/{student_id}")
def patch_student(
    student_id :int,
    name : Optional[str] = None,
    age : Optional[int] = None
):  
    for student in students:
        if student["id"]==student_id:

            if name:
                student["name"]=name
            if age:
                student["age"]= age

                return{
                    "message":"student updated",
                    "student": student
                }
    return {
                "message": "Student not found"
            }
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"]==student_id:
            students.remove(student)

            return {
                "message": "student deleted successfully",
            }
    return{
            "message":"student not found"
        }