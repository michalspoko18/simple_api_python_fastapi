from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
import models
from schemas import ProduktInfo
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/produkt/", status_code=status.HTTP_201_CREATED)
async def stworzProdukt(produkt_info: ProduktInfo, db: db_dependency):
    db_produkt = models.Produkt(
        ID_produktu=produkt_info.ID_produktu,
        Nazwa=produkt_info.Nazwa,
        Opis=produkt_info.Opis,
        Cena=produkt_info.Cena,
        Producent=produkt_info.Producent,
        Kategoria=produkt_info.Kategoria
    )

    db.add(db_produkt)
    db.commit()

@app.get("/produkt/{Nazwa}", status_code = status.HTTP_200_OK)
async def pokazProdukt(Nazwa: str, db: db_dependency):
    produkt = db.query(models.Produkt).filter(models.Produkt.Nazwa == Nazwa).first()
    if produkt is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu")
    return produkt