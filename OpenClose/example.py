##incorrecto

class Form:
    def draw(self):
        print("Form drawn square")
    def draw_circle(self):
        print("Form drawn circle")
        
    def draw_parabole(self):
        print("Form drawn parabole")

##correcto

class Form:
    def draw(self):
        pass
class Square():
    def draw(self):
        print("Square drawn")
class Circle():
    def draw(self):
        print("Circle drawn")
class Parabole():   
    def draw(self):
        print("Parabole drawn")
        