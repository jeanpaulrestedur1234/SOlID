#incorrecto
class Calculadora:
    def calcular(self, operacion, a, b):
        if operacion == 'suma':
            return a + b
        elif operacion == 'resta':
            return a - b
        # Si queremos agregar multiplicación, tenemos que modificar esta clase
        else:
            raise ValueError('Operación no soportada')
#correcto

from abc import ABC, abstractmethod

# Clase base para operaciones
class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

# La calculadora no cambia, solo extendemos nuevas operaciones
class Calculadora:
    def __init__(self):
        self.operations={}
    def add_operation(self,name,operation):
        self.operations[name]=operation
    def calculate(self,name,a,b):
        if name not in self.operations:
            raise ValueError('Operación no soportada')
        
        return self.operations[name].calcular(a,b)
    

# Crear instancia de la calculadora
calculadora = Calculadora()

calculadora.add_operation("suma",Suma())
calculadora.add_operation("resta",Resta())
# Calcular resultados
resultado_suma = calculadora.calculate('suma',10,2)
resultado_resta = calculadora.calculate('resta',10,2)

# Mostrar resultados
print(f"Resultado de la suma: {resultado_suma}")    # Resultado de la suma: 8
print(f"Resultado de la resta: {resultado_resta}")  # Resultado de la resta: 2
