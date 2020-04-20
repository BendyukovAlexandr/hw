# Опишите классы графического объекта, прямоугольника и объекта,
# который может обрабатывать нажатия мыши.
# Опишите класс кнопки.
# Создайте объект кнопки и обычного прямоугольника.
# Вызовите метод нажатия на кнопку.
class Graphic:
    def clicker(self):
        try:
            self.click()
        except AttributeError:
            print("it is",self.__class__.__name__, "can't click")

class Clickaem:
    def click(self):
        print("it is",self.__class__.__name__, ', clickable object')

class Kvadrat(Graphic):
    def __init__(self, dlina, shirina, simbol=""):
        self.dlina=dlina
        self.shirina=shirina
        self.simbol=simbol

    def risuem(self):
        for i in range(self.shirina):
            print(self.simbol*self.dlina)

class Knopka(Kvadrat, Clickaem):
    pass

kvadrat=Kvadrat(25,5,"*")
kvadrat.risuem()
kvadrat.clicker()
knopka=Knopka(25,5,"*")
knopka.risuem()
knopka.clicker()



