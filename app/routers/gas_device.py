from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/data/gas-device", tags=["Gas Device"])

@router.post("/", response_model=schemas.GasDevice)
def create_gas_device(gas_device: schemas.GasDeviceCreate, db: Session = Depends(get_db)):
    db_gas_device = crud.get_gas_device(db, device_id=gas_device.device_id)
    if db_gas_device:
        raise HTTPException(status_code=400, detail="Gas device already registered")
    return crud.create_gas_device(db=db, gas_device=gas_device)

@router.post("/readings", response_model=schemas.GasDeviceReading)
def create_gas_device_reading(gas_device_reading: schemas.GasDeviceReadingCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_gas_device_reading(db=db, gas_device_reading=gas_device_reading)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{device_id}", response_model=schemas.GasDevice)
def read_gas_device(device_id: str, db: Session = Depends(get_db)):
    db_gas_device = crud.get_gas_device(db, device_id=device_id)
    if db_gas_device is None:
        raise HTTPException(status_code=404, detail="Gas device not found")
    return db_gas_device

@router.get("/{device_id}/readings", response_model=List[schemas.GasDeviceReading])
def read_gas_device_readings(device_id: str, db: Session = Depends(get_db)):
    return db.query(models.GasDeviceReading).filter(models.GasDeviceReading.device_id == device_id).all()
