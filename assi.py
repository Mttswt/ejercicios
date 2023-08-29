def escribir_ascii_en_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for i in range(128):
            archivo.write(f"Carácter: {chr(i)} | Código ASCII: {i}\n")

nombre_archivo = "caracteres_ascii.txt"
escribir_ascii_en_archivo(nombre_archivo)
print(f"La lista de caracteres ASCII se ha escrito en el archivo '{nombre_archivo}'.")
