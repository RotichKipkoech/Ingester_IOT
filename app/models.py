from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class GasDevice(Base):
    __tablename__ = 'gas_devices'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, unique=True, index=True)
    battery_status = Column(Float)
    timestamp = Column(DateTime)

class GasDeviceReading(Base):
    __tablename__ = 'gas_device_readings'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    weight_reading = Column(Float)
    timestamp = Column(DateTime)

class WallAdapter(Base):
    __tablename__ = 'wall_adapters'
    id = Column(Integer, primary_key=True, index=True)
    message_count_id = Column(Integer)
    device_id = Column(String, index=True)
    connection_type = Column(String)
    battery_status = Column(Float)
    battery_health = Column(String)
    power_source = Column(String)
    timestamp = Column(DateTime)
