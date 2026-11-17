from calculadorapoo import Operacion, Resta

def main():
    operacion = Operacion(20, 8)
    resta = Resta(20, 8)

    print(f"numero 1: {operacion.num1}")
    print(f"numero 2: {operacion.num2}")
    print(operacion.mostrarResultado())
    print(resta.mostrarResultado())


if __name__ == '__main__':
    main()
