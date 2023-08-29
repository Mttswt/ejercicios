def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

numero = int(input("Ingresa un número para calcular su factorial: "))

factorial = calcular_factorial(numero)

print(f"El factorial de {numero} es {factorial}")
