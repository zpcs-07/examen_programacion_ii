#Desarrolla ejercicio_2/calculadorapoo.py utilizando dos clases: Operacion (padre) y Resta (hija).
#Operacion tendrá un __init__ que reciba y guarde dos números. 
#Operacion tendrá calcular() que regrese la suma de sus dos propiedades. 
#Operacion tendrá mostrarResultado() que llame a calcular() y muestre el resultado. 
#Resta heredará de Operacion y redefinirá calcular() para regresar la resta de las propiedades heredadas. No 
#necesita un constructor nuevo. 
#Solicitar dos números; crear un objeto de Operacion y otro de Resta; llamar a mostrarResultado() en ambos. 
#Mostrar el nombre de la operación desde el programa principal. 
#Guardar evidencia con los valores 20 y 8, y otra ejecución con otros valores.

#Ejemplo: 
    #Número 1: 20 
    #Número 2: 8 
    #Resultado de la suma: 28 
    #Resultado de la resta: 12

class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular(self):
        return self.num1 + self.num2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la suma: {resultado}")

class Resta(Operacion):
    def calcular(self):
        return self.num1 - self.num2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la resta: {resultado}")        