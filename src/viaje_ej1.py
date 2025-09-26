distancia_km = int(input("¿A qué distancia te encuentras?"))  # distancia Tierra - Luna
velocidad_kmh = int(input("¿A qué velocidad vas?"))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")
