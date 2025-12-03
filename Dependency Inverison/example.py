## sin DIP
class Switch:
    def turn_on(self):
        return "on Lamp"
    
    def turn_off(self):
        return "off Lamp"

class Lamp:
    def __init__(self)-> None:
        self.switch = Switch()
    
    
    def operate (self, command):
        if command == "on":
            return self.switch.turn_on()
        elif command == "off":
            return self.switch.turn_off()

lamp = Lamp()
print(lamp.operate("on"))  # Output: Switch is on
print(lamp.operate("off"))  # Output: Switch is off

# solucion
print("-"*100)
from abc import ABC, abstractmethod

# Clase abstracta que define la interfaz del interruptor
class AbstractSwitch(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Implementación concreta del interruptor para una lámpara
class LampSwitch(AbstractSwitch):
    def turn_on(self):
        print(">> Ejecutando LampSwitch.turn_on()")
        return "Lamp is on"
    
    def turn_off(self):
        print(">> Ejecutando LampSwitch.turn_off()")
        return "Lamp is off"

# Clase que representa una lámpara controlada por un interruptor
class Lamp:
    def __init__(self, switch: AbstractSwitch) -> None:
        print(">> Creando objeto Lamp con interruptor:", switch.__class__.__name__)
        self.switch = switch
    
    def operate(self, command):
        print(f">> Recibido comando: {command}")
        if command == "on":
            return self.switch.turn_on()
        elif command == "off":
            return self.switch.turn_off()
        else:
            return "Comando inválido"

# === Simulación ===
lamp = Lamp(LampSwitch())

print(lamp.operate("on"))   # Debe encender la lámpara
print(lamp.operate("off"))  # Debe apagar la lámpara
print(lamp.operate("blink"))  # Comando no válido
