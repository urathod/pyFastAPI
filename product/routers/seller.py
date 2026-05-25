from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ..schemas import DisplayProduct, DisplaySeller, Product, Seller
from ..import models, schemas
from ..database import SessionLocal, get_db
from passlib.context import CryptContext

router = APIRouter(
    prefix="/seller",
    tags=["Sellers"]
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=DisplaySeller, status_code=status.HTTP_201_CREATED)
async def create_seller(seller: Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(seller.password)
    db_seller = models.Seller(id = seller.id, username=seller.username, email=seller.email, password=hashed_password)
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller