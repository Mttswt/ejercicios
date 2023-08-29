def convertir_a_romano(digito, uno, cinco, diez):
    if digito == 0:
        return ""
    elif digito <= 3:
        return uno * digito
    elif digito == 4:
        return uno + cinco
    elif digito <= 8:
        return cinco + uno * (digito - 5)
    else:
        return uno + diez

def numero_a_romano(numero):
    if numero < 1 or numero > 999:
        return "Número fuera de rango"
    
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    
    romano_centenas = convertir_a_romano(centenas, "C", "D", "M")
    romano_decenas = convertir_a_romano(decenas, "X", "L", "C")
    romano_unidades = convertir_a_romano(unidades, "I", "V", "X")
    
    numero_romano = romano_centenas + romano_decenas + romano_unidades
    return numero_romano

numero = int(input("Ingresa un número entre 0 y 999: "))

numero_romano = numero_a_romano(numero)

print(f"El número {numero} en números romanos es: {numero_romano}")