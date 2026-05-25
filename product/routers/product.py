from fastapi import APIRouter, Depends, status, Response, HTTPException
from product.routers.login import get_current_user
from sqlalchemy.orm import Session
from ..schemas import DisplayProduct, DisplaySeller, Product, Seller
from ..import models, schemas
from ..database import SessionLocal, get_db

router = APIRouter(
    prefix="/product",
    tags=["Products"]
)

@router.get("/{product_id}", response_model=DisplayProduct)
async def get_product(product_id: int, response: Response, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        print("Product not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product

@router.get("/", response_model=list[DisplayProduct])
async def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    db_product = models.Product(name=product.name, price=product.price, description=product.description, seller_id=1)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted successfully"}

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.price = product.price
    db_product.description = product.description
    db.commit()
    db.refresh(db_product)
    return db_product
