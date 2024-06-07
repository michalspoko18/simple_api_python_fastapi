from sqlalchemy import Boolean, Column, Integer, String, Text, Numeric, JSON, Date, ForeignKey
from database import Base

class Produkt(Base):
    __tablename__ = 'Produkt'

    ID_produktu = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nazwa = Column(String(100), index=True, nullable=True, unique=True)
    Opis = Column(Text, nullable=True)
    Cena = Column(Numeric(10, 2), nullable=True)
    Producent = Column(String(100), nullable=True)
    Kategoria = Column(String(100), nullable=True)


class Klient(Base):
    __tablename__ = 'Klient'

    ID_Klienta = Column(Integer, primary_key=True, index=True)
    Imie = Column(String(50), nullable=False)
    Nazwisko = Column(String(50), nullable=False)
    Email = Column(String(100), nullable=False)
    Telefon = Column(String(15), nullable=False)
    Ulica = Column(String(100), nullable=True)
    Nr = Column(String(15), nullable=True)
    Kod_pocztowy = Column(String(6), nullable=True)
    Miasto = Column(String(100), nullable=True)


class Recepta(Base):
    __tablename__ = 'Recepta'

    ID_Recepty = Column(Integer, primary_key=True, index=True)
    Pin_Recepty = Column(Integer, nullable=False)
    ID_Klienta = Column(Integer, ForeignKey('Klient.ID_Klienta'), nullable=False)
    Data = Column(Date, nullable=False)
    Opis = Column(JSON, nullable=False)