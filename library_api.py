print("==========Library_API=========")
from fastapi import FastAPI
books = [
    {"id":2,"chapters":2,"chapter_id": 134},
    {"id":3,"chapters":4,"chapter_id": 123}
]
app  = FastAPI()
@app.get("/books")
def get():
    return books
@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"] ==book_id:
            return book
    return{
        "message": "Book not found"
    }
@app.get("/books/{book_id}/chapters/{chapter_id}")
def get_book_chapters(book_id:int,chapter_id:int):
    for book in books:
        if book["id"]==book_id and book["chapter_id"] ==chapter_id:
            return{
                "book": book_id,
                "chapter": chapter_id
            }
    return{
        "message":"Book not found"
    }