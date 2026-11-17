from estacionamiento import Estacionamiento
def main():
    horas1 = Estacionamiento(2)
    horas2 = Estacionamiento(4)
    horas3 = Estacionamiento(6)

    print(horas1.mostrarRecibo())
    print(horas2.mostrarRecibo())
    print(horas3.mostrarRecibo())


if __name__ == '__main__':
    main()

