from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import date

class ProduktInfo(BaseModel):
    ID_Produktu: Optional[int] = None
    Nazwa: str
    Opis: str
    Cena: float
    Producent: str
    Kategoria: str

class ProduktModyfikacja(BaseModel):
    Nazwa: Optional[str]
    Opis: Optional[str] 
    Cena: Optional[float]
    Producent: Optional[str]
    Kategoria: Optional[str]

class ReceptaInfo(BaseModel):
    Pin_Recepty: int
    ID_Klienta: int
    Data: date
    Opis: Dict[str, Any]

class ReceptaModyfikacja(BaseModel):
    Opis: Dict[str, Any]

class KlientInfo(BaseModel):
    ID_Klienta: int
    Imie: str
    Nazwisko: str
    Email: str
    Telefon: str
    Ulica: str 
    Nr: str
    Kod_pocztowy: str
    Miasto: str
