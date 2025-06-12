# Simple Python FastAPI Project

Ten projekt implementuje interfejs REST API do zarządzania danymi związanymi z farmacją przy użyciu FastAPI, SQLAlchemy i MySQL.

## Przegląd

API udostępnia endpointy do zarządzania:
- Produktami (farmaceutykami)
- Receptami
- Klientami

## Konfiguracja

### Wymagania wstępne
- Python 3.11+
- Baza danych MySQL

### Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/yourusername/simple_api_python_fastapi.git
cd simple_api_python_fastapi
```

2. Utwórz i aktywuj środowisko wirtualne:
```bash
python -m venv env
source env/bin/activate  # W systemie Windows: env\Scripts\activate
```

3. Zainstaluj zależności:
```bash
pip install fastapi sqlalchemy pymysql uvicorn pydantic
```

4. Zaktualizuj ciąg połączenia z bazą danych w pliku `database.py`:
```python
URL_DATABASE = 'mysql+pymysql://username:password@localhost/database_name'
```

5. Uruchom serwer:
```bash
uvicorn main:app --reload
```

## Endpointy API

### Produkty

- `GET /produkt/{Nazwa}` - Pobieranie produktu po nazwie
- `GET /produkt/` - Pobieranie wszystkich produktów
- `POST /produkt/` - Tworzenie nowego produktu
- `PUT /produkt/{produkt_id}` - Aktualizacja istniejącego produktu
- `DELETE /produkt/{Nazwa}` - Usuwanie produktu po nazwie

### Recepty

- `GET /recepta/{pin_recepty}:{pesel}` - Pobieranie recepty przy użyciu PIN i numeru PESEL klienta
- `PUT /recepta/{pin_recepty}:{pesel}` - Aktualizacja recepty

## Modele danych

### Produkt
- ID_produktu: Unikalny identyfikator
- Nazwa: Nazwa produktu
- Opis: Opis
- Cena: Cena
- Producent: Producent
- Kategoria: Kategoria

### Klient
- ID_Klienta: Identyfikator klienta (PESEL)
- Imie: Imię
- Nazwisko: Nazwisko
- Email: Adres email
- Telefon: Numer telefonu
- Dane adresowe (Ulica, Nr, Kod_pocztowy, Miasto)

### Recepta
- ID_Recepty: Unikalny identyfikator
- Pin_Recepty: PIN recepty
- ID_Klienta: Identyfikator klienta (klucz obcy)
- Data: Data
- Opis: Opis (format JSON)

## Przykłady

### Tworzenie produktu

```json
POST /produkt/
{
  "Nazwa": "Aspiryna",
  "Opis": "Środek przeciwbólowy",
  "Cena": 9.99,
  "Producent": "Bayer",
  "Kategoria": "Leki przeciwbólowe"
}
```

### Pobieranie recepty

```
GET /recepta/123456:12345678901
```

## Rozwój projektu

Projekt wykorzystuje:
- FastAPI jako framework webowy
- SQLAlchemy do mapowania obiektowo-relacyjnego (ORM)
- Pydantic do walidacji danych