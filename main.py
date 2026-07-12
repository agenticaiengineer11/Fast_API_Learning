from fastapi import FastAPI,Query

# Create the FastAPI application
app = FastAPI()

# About Route
@app.get("/about")
def about():
    return {
        "name": "Noman Ali",
        "course": "BS Software Engineering",
        "goal": "Become an AI Engineer"
    }

# Contact Route
@app.get("/contact")
def contact():
    return {
        "email": "noman@example.com",   # Replace with your real email if you want
        "country": "Pakistan"
    }

@app.get("/laptops")
def get_laptops(brand:str = Query(min_length=2,max_length=15)):
    return{
        "brand": brand
    }

@app.get("/employees/search")
def search_employees(
    name: str = Query(min_length=3, max_length=30),
    salary: int = Query(gt=20000, le=500000)
):
    return {
        "name": name,
        "salary": salary
    }