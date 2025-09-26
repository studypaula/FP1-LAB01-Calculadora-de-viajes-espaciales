edad = int(input("¿Cuántos años tienes?"))
nivel_fisico = int(input("Elige tu nivel físico del 1 al 10"))
if edad <18:
    print("Debes ser mayor de edad.")
elif nivel_fisico <5:
    print("Debes estar en mejor forma.")
else:
    print("¡Listo para despegar!")
