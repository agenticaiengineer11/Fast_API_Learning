from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/employee")
def employee():
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Employee</title>
        </head>
        <body>
            <h1>Employee Management System</h1>

            <h2>Employee Information</h2>

            <p>Name: Noman</p>
            <p>Department: Finance</p>
            <p>Salary: 60,000</p>
        </body>
        </html>
        """
    )