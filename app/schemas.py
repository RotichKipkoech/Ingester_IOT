from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class GasDeviceBase(BaseModel):
    device_id: str
    battery_status: float
    timestamp: datetime

class GasDeviceCreate(GasDeviceBase):
    pass

class GasDevice(GasDeviceBase):
    id: int

    class Config:
        orm_mode = True

class GasDeviceReadingBase(BaseModel):
    device_id: str
    weight_reading: float
    timestamp: datetime

class GasDeviceReadingCreate(GasDeviceReadingBase):
    pass

class GasDeviceReading(GasDeviceReadingBase):
    id: int

    class Config:
        orm_mode = True

class WallAdapterBase(BaseModel):
    message_count_id: int
    device_id: str
    connection_type: str
    battery_status: float
    battery_health: str
    power_source: str
    timestamp: datetime

class WallAdapterCreate(WallAdapterBase):
    pass

class WallAdapter(WallAdapterBase):
    id: int

    class Config:
        orm_mode = True
