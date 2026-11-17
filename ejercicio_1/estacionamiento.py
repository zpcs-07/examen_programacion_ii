#Un estacionamiento cobra por hora según la duración total de la estancia:
#Horas | Tarifa por hora
#1 a 2 | $15
#3 a 5 | $12
#mas de 5 | $10

#La tarifa del rango correspondiente se aplica a TODAS las horas registradas.
#Crear la clase Estacionamiento. Su constructor __init__ recibe horas y las guarda como propiedad. 
#Crear calcularPago() para devolver el importe total calculado con if/elif/else. 
#Crear mostrarRecibo() que utilice calcularPago() y muestre horas e importe con dos decimales. 
#En el programa principal, solicitar las horas, comprobar que sea un entero mayor que cero, crear un objeto y 
#llamar a mostrarRecibo(). 
#Ejecutar al menos los casos de 2, 4 y 6 horas; guardar capturas de dos ejecuciones.

#Ejemplo (4 horas): 
#Horas estacionadas: 4 
#RECIBO DE ESTACIONAMIENTO 
#Horas: 4 
#Total a pagar: $48.00

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

