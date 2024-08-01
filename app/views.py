# app/views.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, controller
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return controller.create_address(db, address)

@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = controller.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    db_address = controller.update_address(db, address_id, address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.delete("/addresses/{address_id}", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = controller.delete_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses_within_distance(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    return controller.get_addresses_within_distance(db, lat, lon, distance)
