from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ProduktInfo(BaseModel):
    ID_Produktu: Optional[int] = None
    Nazwa: str
    Opis: str
    Cena: float
    Producent: str
    Kategoria: str

class ProduktAktualizacja(BaseModel):
    Nazwa: Optional[str]
    Opis: Optional[str] 
    Cena: Optional[float]
    Producent: Optional[str]
    Kategoria: Optional[str]

class ReceptaInfo(BaseModel):
    ID_Recepty: int
    ID_Klienta: int
    Data: date
    Opis: str

class KlientInfo(BaseModel):
    ID_Klienta: int
    Imie: str
    Nazwisko: str
    Email: str
    Telefon: str
    Ulica: str