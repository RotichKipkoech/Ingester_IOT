from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/data/wall-adapter", tags=["Wall Adapter"])

@router.post("/", response_model=schemas.WallAdapter)
def create_wall_adapter(wall_adapter: schemas.WallAdapterCreate, db: Session = Depends(get_db)):
    return crud.create_wall_adapter(db=db, wall_adapter=wall_adapter)

@router.get("/", response_model=List[schemas.WallAdapter])
def read_wall_adapters(db: Session = Depends(get_db)):
    return db.query(models.WallAdapter).all()
