from pydantic import BaseModel

class ProduktInfo(BaseModel):
    Nazwa: str
    Opis: str
    Cena: float
    Producent: str
    Kategoria: str