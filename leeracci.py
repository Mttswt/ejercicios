def leer_y_mostrar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

nombre_archivo = "caracteres_ascii.txt"
leer_y_mostrar_archivo(nombre_archivo)