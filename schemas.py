from pydantic import BaseModel

class ProduktInfo(BaseModel):
    ID_produktu: int
    Nazwa: str
    Opis: str
    Cena: float
    Producent: str
    Kategoria: str

    class Config:
        orm_mode = True