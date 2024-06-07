from sqlalchemy import Boolean, Column, Integer, String, Text, Numeric
from database import Base

class Produkt(Base):
    __tablename__ = 'Produkt'

    ID_produktu = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nazwa = Column(String(100), index=True, nullable=True, unique=True)
    Opis = Column(Text, nullable=True)
    Cena = Column(Numeric(10, 2), nullable=True)
    Producent = Column(String(100), nullable=True)
    Kategoria = Column(String(100), nullable=True)