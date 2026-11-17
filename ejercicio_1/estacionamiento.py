
class Estacionamiento: 
    def __init__(self, horas):
        self.horas = horas
    
    def calcularPago(self):
        if self.horas >= 1 and self.horas <= 2:
            tarifa = 15
        elif self.horas >= 3 and self.horas <= 5:
            tarifa = 12
        else:
            tarifa = 10
        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()
        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}")

