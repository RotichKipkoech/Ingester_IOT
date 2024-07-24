from fastapi import FastAPI
from .routers import gas_device, wall_adapter

app = FastAPI()

app.include_router(gas_device.router)
app.include_router(wall_adapter.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the IoT Data Ingestion API"}
