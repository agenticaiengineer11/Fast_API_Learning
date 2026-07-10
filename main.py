from fastapi import FastAPI

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