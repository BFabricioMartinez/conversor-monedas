def convertir(moneda_origen, moneda_destino, cantidad):
    tasas = {
        "USD": 1,
        "EUR": 0.85,
        "ARS": 1250
    }
    if moneda_origen not in tasas or moneda_destino not in tasas:
        return "Moneda no válida"
    return cantidad * tasas[moneda_destino] / tasas[moneda_origen]

print(convertir("USD", "EUR", 100))
