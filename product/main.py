from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import DisplayProduct, DisplaySeller, Product, Seller
from . import models
from .database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from passlib.context import CryptContext

app = FastAPI(
    title="Product API",
    description="API for managing products and sellers",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Uttam Rathod",
        "email": "uttamrathod@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    #docs_url="/documentation",
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db       
    finally:
        db.close()

@app.get("/product/{product_id}", response_model=DisplayProduct, tags=["Products"])
async def get_product(product_id: int, response: Response, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        print("Product not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product

@app.get("/products/", response_model=list[DisplayProduct], tags=["Products"])
async def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, price=product.price, description=product.description, seller_id=1)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/product/{product_id}", tags=["Products"])
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted successfully"}

@app.put("/product/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.price = product.price
    db_product.description = product.description
    db.commit()
    db.refresh(db_product)
    return db_product

@app.post("/sellers/", response_model=DisplaySeller, status_code=status.HTTP_201_CREATED, tags=["Sellers"])
async def create_seller(seller: Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(seller.password)
    db_seller = models.Seller(id = seller.id, username=seller.username, email=seller.email, password=hashed_password)
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller