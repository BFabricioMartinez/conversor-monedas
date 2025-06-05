def convertir(moneda_origen, moneda_destino, cantidad):
    tasas = {
        "USD": 1,
        "EUR": 0.85,
        "ARS": 1250
    }
    if moneda_origen not in tasas or moneda_destino not in tasas:
        return "Moneda no válida"
    return cantidad * tasas[moneda_destino] / tasas[moneda_origen]

try:
    print(convertir("USD", "EUR", 100))  # Ejemplo de uso rápido

    moneda_origen = input("Moneda de origen (USD, EUR, ARS): ")
    moneda_destino = input("Moneda destino (USD, EUR, ARS): ")
    cantidad = float(input("Cantidad a convertir: "))

    resultado = convertir(moneda_origen, moneda_destino, cantidad)
    print(f"{cantidad} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")

except ValueError:
    print("Debe ingresar un número válido")
    exit()
