from fastapi import FastAPI

app = FastAPI()

dolar = (
    {"Moeda": "Dolar", "Code": "USD", "Valor": 5.19,"Ultima atualizaçao": "22/02/2023"},
)

euro = (
    {"Moeda": "Euro", "Code": "EUR", "Valor": 5.50, "Ultima atualizaçao": "22/02/2023"},
)

pesos = (
    {"Moeda": "Pesos", "Code": "PES", "Valor": 0.0027, "Ultima atualizaçao": "22/02/2023"},
)

bitcoin = (
    {"Moeda": "Bitcoin", "Code": "BTC", "Valor": 120.885, "Ultima atualizaçao": "22/02/2023"},
)

@app.get("/dolar")
def get_dolar():
    return dolar

@app.get("/euro")
def get_euro():
    return euro

@app.get("/pesos")
def get_pesos():
    return pesos

@app.get("/bitcoin")
def get_bitcoin():
    return bitcoin

@app.get("/moedas")
def get_moedas():
    return dolar, euro, pesos, bitcoin