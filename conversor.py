from datetime import datetime

def convertir(moneda_origen, moneda_destino, cantidad):
    tasas = {
        "USD": 1,
        "EUR": 0.85,
        "ARS": 1250
    }
    moneda_origen = moneda_origen.upper()
    moneda_destino = moneda_destino.upper()
    
    if moneda_origen not in tasas or moneda_destino not in tasas:
        return "Moneda no válida"
    return cantidad * tasas[moneda_destino] / tasas[moneda_origen]

print("Fecha y hora de la conversión:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print()


def mostrar_tasas():
    print("Tasas de conversión actuales:")
    print("1 USD = 0.85 EUR")
    print("1 USD = 1250 ARS")
    print("1 EUR = 1470.59 ARS")  # 1250 / 0.85
    print("1 EUR = 1.18 USD")     # 1 / 0.85
    print("1 ARS = 0.0008 USD")   # 1 / 1250
    print("1 ARS = 0.00068 EUR")  # 1 / (1250 / 0.85)
    print()

try:
    mostrar_tasas()  # Mostrar tasas al inicio

    moneda_origen = input("Moneda de origen (USD, EUR, ARS): ")
    moneda_destino = input("Moneda destino (USD, EUR, ARS): ")
    cantidad = float(input("Cantidad a convertir: "))

    resultado = convertir(moneda_origen, moneda_destino, cantidad)
    print(f"{cantidad} {moneda_origen.upper()} equivalen a {resultado:.2f} {moneda_destino.upper()}")

except ValueError:
    print("Debe ingresar un número válido")
    exit()
