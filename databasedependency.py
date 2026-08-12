print("===========Database Dependency=================")

from fastapi import FastAPI, Depends,Query

app = FastAPI()

def get_database():
    db = "Database Connection"

    try:
        yield db
    finally:
        print("Database Connection Closed")
@app.get("/students")
def get_student(
        db = Depends(get_database)
):
    return {
        "students":"Students fetched",
        "database": db
    }

