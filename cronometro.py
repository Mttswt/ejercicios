import time

def cronometrar_tiempo(tiempo_limite):
    tiempo_restante = tiempo_limite
    while tiempo_restante >= 0:
        horas = tiempo_restante // 3600
        minutos = (tiempo_restante % 3600) // 60
        segundos = tiempo_restante % 60
        
        print(f"Tiempo restante: {horas:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)
        
        tiempo_restante -= 1

def main():
    try:
        horas = int(input("Ingrese el tiempo en horas: "))
        minutos = int(input("Ingrese el tiempo en minutos: "))
        segundos = int(input("Ingrese el tiempo en segundos: "))
        tiempo_limite = horas * 3600 + minutos * 60 + segundos
    except ValueError:
        print("Debe ingresar valores numéricos válidos.")
        return

    print("Comenzando cronómetro...")
    cronometrar_tiempo(tiempo_limite)
    print("Cronómetro finalizado.")

if __name__ == "__main__":
    main()
