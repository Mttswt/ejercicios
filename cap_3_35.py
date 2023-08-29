def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero = int(input("Ingresa un número para calcular su factorial: "))
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es {resultado}.")
