#Actividad 1. Identificar elementos de POO (12 puntos)
class Producto(object): 
    def __init__(self, nombre, precio): 
        self.nombre = nombre 
        self.precio = precio 
        self.total = 0 
        
    def calcularTotal(self, cantidad): 
        self.total = self.precio * cantidad 

    def mostrarTotal(self): 
        print(f"Producto: {self.nombre}") 
        print(f"Total: ${self.total:.2f}") 
producto1 = Producto("Cuaderno", 35) 
producto1.calcularTotal(3) 
producto1.mostrarTotal() 

1. ¿Cuál es el nombre de la clase? 
#Producto
2. ¿Cuáles son sus propiedades? 
#nombre, precio, total
3. ¿Cuáles son sus métodos? 
#calcularTotal, mostrarTotal
4. ¿Qué función cumple __init__? 
#Inicializa las propiedades del objeto
5. ¿Para qué se utiliza self? 
#Para referirse a las propiedades y métodos del objeto actual
6. ¿En qué instrucción se crea un objeto? 
#producto1 = Producto("Cuaderno", 35)
7. ¿Cuál es el nombre del objeto? 
#producto1
8. ¿Cómo se llama a calcularTotal()? 
#producto1.calcularTotal()
9. ¿Qué valores recibe el constructor cuando se crea el objeto? 
#("Cuaderno", 35)
10. ¿Qué resultado mostrará el programa?
#Producto: Cuaderno
#Total: $105.00


#Actividad 2. Completar código (10 puntos)
class Rectangulo(object): 
    def __init__(self, base, altura): 
        # COMPLETAR: guardar las propiedades 
        self.base = base
        self.altura = altura

    def calcularArea(self): 
        # COMPLETAR: regresar el área 
        return self.base * self.altura

    def mostrarArea(self): 
        # COMPLETAR: mostrar el resultado 
        print(f"Área: {self.calcularArea()}")

# COMPLETAR: crear un objeto con base 8 y altura 5
rectangulo1 = Rectangulo(8, 5)
# COMPLETAR: llamar al método para mostrar el área
rectangulo1.mostrarArea()


#Actividad 3. Interpretar herencia (8 puntos)
class Operacion(object): 
    def __init__(self, numero1, numero2): 
        self.numero1 = numero1 
        self.numero2 = numero2 
  
    def calcular(self): 
        return self.numero1 + self.numero2 
  
class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2

operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular()) 

1. ¿Cuál es la clase padre? 
#Operacion
2. ¿Cuál es la clase hija? 
#Multiplicacion
3. ¿Cómo se indica la herencia? 
#Poniendo dentro del parentesis de la clase hija el nombre de la clase padre
4. ¿Qué propiedades utiliza la clase hija? 
#numero1, numero2
5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
#Porque hereda el __init__ de la clase padre
6. ¿Por qué los métodos calcular() tienen resultados distintos? 
#Porque la clase hija redefine el método calcular()
7. ¿Qué valores se imprimen? 
#12
#32
8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
#Se utilizaría el método calcular() de la clase padre, imprimiendo 12