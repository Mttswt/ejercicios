def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
x = int(input("Ingrese el valor de x para calcular el término correspondiente en la serie de Fibonacci: "))

resultado = fibonacci(x)
print(f"El término {x} de la serie de Fibonacci es {resultado}")