from fastapi import FastAPI, Depends, Query, HTTPException, APIRouter

app = FastAPI()


def get_pagination(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50)
):
    return {
        "page": page,
        "limit": limit
    }

def get_current_user():
    return {
        "id": 1,
        "name": "Muku",
        "role": "admin"
    }

def require_admin(
    user=Depends(get_current_user)
):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin permission required"
        )

    return user

product_router = APIRouter(
    prefix="/products",
    tags=["Products"],
    dependencies=[Depends(require_admin)]
)


@product_router.get("/")
def get_products(
    pagination=Depends(get_pagination)
):
    return {
        "products": ["Mobile", "Laptop"],
        "pagination": pagination
    }


@product_router.get("/{product_id}")
def get_product(product_id: int):
    return {
        "product": "iPad",
        "product_id": product_id
    }

@product_router.post("/")
def create_product():
    return {
        "message": "Product created"
    }
@product_router.delete("/{product_id}")
def delete_product(product_id: int):
    return {
        "message": "Product deleted",
        "product_id": product_id
    }


app.include_router(product_router)