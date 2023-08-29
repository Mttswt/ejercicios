def contar_caracteres(cadena, vocales, consonantes):
    num_vocales = 0
    num_consonantes = 0
    num_no_pertenecen = 0

    for char in cadena:
        if char.lower() in vocales:
            num_vocales += 1
        elif char.lower() in consonantes:
            num_consonantes += 1
        else:
            num_no_pertenecen += 1
    
    return num_vocales, num_consonantes, num_no_pertenecen


vocales = ('a', 'e', 'i', 'o', 'u')
consonantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

cadena = input("Ingresa una cadena de caracteres: ")


num_vocales, num_consonantes, num_no_pertenecen = contar_caracteres(cadena, vocales, consonantes)


print(f"Número de vocales: {num_vocales}")
print(f"Número de consonantes: {num_consonantes}")
print(f"Número de caracteres que no pertenecen a ninguna categoría: {num_no_pertenecen}")