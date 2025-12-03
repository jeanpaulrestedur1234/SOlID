##incorrecto
class Bird:
    def fly(self):
        return "I can fly"

class Duck(Bird):
    def fly(self):
        print("[Duck] Intentando volar...")
        resultado = super().fly()
        print(f"[Duck] Resultado de vuelo heredado: {resultado}")
        return resultado

class Chicken(Bird):
    def fly(self):
        print("[Chicken] Intentando volar...")
        raise Exception("Los pollos no pueden volar")

# Instancia de Bird
bird = Bird()
print("== Bird ==")
print("Resultado:", bird.fly())
print()

# Instancia de Duck
duck = Duck()
print("== Duck ==")
print("Resultado:", duck.fly())
print()

# Instancia de Chicken
chicken = Chicken()
print("== Chicken ==")
try:
    print("Resultado:", chicken.fly())
except Exception as e:
    print("Error:", e)

### correcto
print('_'*100)






from abc import ABC, abstractmethod
# Clase abstracta base
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

# Subclase para aves que vuelan
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

    def move(self):
        return "Me muevo volando"

# Subclase para aves que no vuelan
class NonFlyingBird(Bird):
    def move(self):
        return "Me muevo caminando"

# Implementaciones concretas
class Duck(FlyingBird):
    def fly(self):
        return "El pato está volando"

    def move(self):
        # Usa super() para extender el comportamiento de FlyingBird
        return f"{super().move()} y también nado"

class Chicken(NonFlyingBird):
    def move(self):
        # Usa super() para mantener el comportamiento base
        return f"{super().move()} y picoteo el suelo"

# Funciones que usan las clases base
def move_bird(bird: Bird):
    print(f"[{bird.__class__.__name__}] Movimiento: {bird.move()}")

def make_it_fly(bird: FlyingBird):
    print(f"[{bird.__class__.__name__}] Vuelo: {bird.fly()}")

# Ejecución de pruebas
duck = Duck()
chicken = Chicken()

print("== PRUEBAS DE MOVIMIENTO ==")
move_bird(duck)       # ✔ Duck puede moverse (volando y nadando)
move_bird(chicken)    # ✔ Chicken puede moverse (caminando y picoteando)

print("\n== PRUEBAS DE VUELO ==")
make_it_fly(duck)     # ✔ Duck puede volar