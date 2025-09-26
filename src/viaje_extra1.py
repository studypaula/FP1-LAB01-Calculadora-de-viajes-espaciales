distancia = int(input("¿Cuál es la distancia qué buscas recorrer?"))
distancia_max = 150000
x = 0
while distancia > 150000:
    distancia -= distancia_max
    x += 1
    print(f"Parada en el km {distancia_max*x}")
print(f"Total de paradas para repostar: {x}.")


