print("==========Library_API=========")
from fastapi import FastAPI,Query
books = [
    {"id":2,"title":"python","chapter_id": 134},
    {"id":3,"title":"c++","chapter_id": 123}
]
app  = FastAPI()
@app.get("/books")
def get():
    return books

@app.get("/books/search")
def search_book(book_id:int, 
                title:str=Query(min_length=3,max_length=20,description="Enter the book title ",example="Python")
                ):
    for book in books:
        if book["title"] == title and book["id"] == book_id:
            return book
    return {
        "message": "Not found"
    }
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

