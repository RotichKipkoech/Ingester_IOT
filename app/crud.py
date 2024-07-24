from sqlalchemy.orm import Session
from . import models, schemas

def create_gas_device(db: Session, gas_device: schemas.GasDeviceCreate):
    db_gas_device = models.GasDevice(**gas_device.dict())
    db.add(db_gas_device)
    db.commit()
    db.refresh(db_gas_device)
    return db_gas_device

def get_gas_device(db: Session, device_id: str):
    return db.query(models.GasDevice).filter(models.GasDevice.device_id == device_id).first()

def create_gas_device_reading(db: Session, gas_device_reading: schemas.GasDeviceReadingCreate):
    db_gas_device_reading = models.GasDeviceReading(**gas_device_reading.dict())
    db.add(db_gas_device_reading)
    db.commit()
    db.refresh(db_gas_device_reading)
    return db_gas_device_reading

def create_wall_adapter(db: Session, wall_adapter: schemas.WallAdapterCreate):
    db_wall_adapter = models.WallAdapter(**wall_adapter.dict())
    db.add(db_wall_adapter)
    db.commit()
    db.refresh(db_wall_adapter)
    return db_wall_adapter
