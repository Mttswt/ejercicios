from funciones_aritmeticas81 import suma, resta, multiplicacion, division, potencia


def main():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Debe ingresar números enteros válidos.")
        return

    print("Suma:", suma(a, b))
    print("Resta:", resta(a, b))
    print("Multiplicación:", multiplicacion(a, b))
    
    try:
        print("División:", division(a, b))
    except ValueError as e:
        print(e)
        
    print("Potencia:", potencia(a, b))

if __name__ == "__main__":
    main()