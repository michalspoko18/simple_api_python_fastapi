from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
import models
from schemas import *
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date


app = FastAPI()
dzisiaj = date.today()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/produkt/{Nazwa}", status_code = status.HTTP_200_OK)
async def pokazProdukt(Nazwa: str, db: db_dependency):
    produkt = db.query(models.Produkt).filter(models.Produkt.Nazwa == Nazwa).first()
    if produkt is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu")
    return produkt

@app.get("/produkt/", status_code = status.HTTP_200_OK)
async def pokazProdukty(db: Session = Depends(get_db)):
    produkty = db.query(models.Produkt).all()
    if produkty is None:
        raise HTTPException(status_code=404, detail="Brak produktow")
    return {'ilosc produktow': len(produkty),'produkty': produkty}


@app.post("/produkt/", status_code=status.HTTP_201_CREATED)
async def stworzProdukt(produkt_info: ProduktInfo, db: db_dependency):
    db_produkt = models.Produkt(
        Nazwa=produkt_info.Nazwa,
        Opis=produkt_info.Opis,
        Cena=produkt_info.Cena,
        Producent=produkt_info.Producent,
        Kategoria=produkt_info.Kategoria
    )

    db.add(db_produkt)
    db.commit()
    raise HTTPException(status_code=200, detail=f"Produkt {produkt_info.Nazwa} zostal dodany do bazy")

@app.put("/produkt/{produkt_id}", status_code=status.HTTP_200_OK)
async def aktualizujProdukt(produkt_id: int, produkt_info: ProduktModyfikacja, db: db_dependency):
    produkt = db.query(models.Produkt).filter(models.Produkt.ID_produktu == produkt_id).first()
    if produkt is None:
        raise HTTPException(status_code=404, detail="Produkt nie znaleziony")

    for field, value in produkt_info.dict(exclude_unset=True).items():
        setattr(produkt, field, value)

    db.commit()
    db.refresh(produkt)
    return produkt

@app.delete("/produkt/{Nazwa}", status_code=status.HTTP_200_OK)
async def usunProdukt(Nazwa: str, db: db_dependency):
    produkt = db.query(models.Produkt).filter(models.Produkt.Nazwa == Nazwa).first()
    nazwa_produktu = produkt.Nazwa
    if produkt is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu")
    db.delete(produkt)
    db.commit()
    raise HTTPException(status_code=200, detail=f"Produkt {nazwa_produktu} zostal usuniety")

@app.get("/recepta/{pin_recepty}:{pesel}", status_code=status.HTTP_200_OK, response_model=ReceptaInfo)
async def pokazRecepte(pin_recepty: int, pesel: int, db: Session = Depends(get_db)):
    recepta = db.query(models.Recepta).filter(
        models.Recepta.Pin_Recepty == pin_recepty,
        models.Recepta.ID_Klienta == pesel,
    ).first()
    
    if recepta is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono recepty")
    
    if recepta.Data < dzisiaj:
        raise HTTPException(status_code=400, detail="Recepta jest przeterminowana")
    
    return recepta

@app.put("/recepta/{pin_recepty}:{pesel}")
async def aktualizujRecepte(pin_recepty: int, pesel: int, recepta_info: ReceptaModyfikacja, db: Session = Depends(get_db)):
    recepta = db.query(models.Recepta).filter(
        models.Recepta.Pin_Recepty == pin_recepty,
        models.Recepta.ID_Klienta == pesel,
    ).first()

    if recepta is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono recepty")
    
    if recepta.Data < dzisiaj:
        raise HTTPException(status_code=400, detail="Recepta jest przeterminowana")

    for field, value in recepta_info.dict(exclude_unset=True).items():
        setattr(recepta, field, value)

    db.commit()
    db.refresh(recepta)
    return recepta