def eliminar_blancos(cadena):
    cadena_sin_blancos = cadena.replace(" ", "")
    return cadena_sin_blancos

cadena_original = input("Ingresa una cadena de caracteres: ")

cadena_transformada = eliminar_blancos(cadena_original)

print("Cadena original:", cadena_original)
print("Cadena transformada:", cadena_transformada)
