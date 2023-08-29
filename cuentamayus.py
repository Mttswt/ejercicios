def contar_mayusculas(cadena):
    contador = 0
    for char in cadena:
        if char.isupper():
            contador += 1
    return contador

cadena = input("Ingresa una cadena de caracteres: ")

cantidad_mayusculas = contar_mayusculas(cadena)



print(f"Cantidad de mayúsculas en la cadena: {cantidad_mayusculas}")