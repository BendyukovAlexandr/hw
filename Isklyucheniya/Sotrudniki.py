# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
# Конструктор должен генерировать исключение, если заданы неправильные данные.
# Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.

class Rab:
    def __init__(self, name, family, otdel, year_begin):
        self.name=name
        self.family=family
        self.otdel=otdel
        self.year_begin=year_begin


    def vvod():
         name=input("name ")
         if not name:
             raise ValueError("empty name")
         family=input("family ")
         if not family:
             raise ValueError("empty family")
         otdel=input("otdel ")
         if not otdel:
             raise ValueError("empty otdel")
         year_begin=int(input("year "))
         if not year_begin:
             raise ValueError("empty nachalo raboty")
         elif not year_begin >= 2007:
             raise ValueError("firma osnovana v 2007, nevozmozhno nachat' rabotat' ran'she")
         return Rab(name, family, otdel, year_begin)

    def __repr__(self):
        return ("Rabs:({name},{family},{otdel},{year_begin})").format_map(self.__dict__)

def esche():
    rabs=[]
    a="+"
    if a == "+":
        while a=="+":
            try:
                rab=Rab.vvod()
            except ValueError as error:
                print("Error:", error)
            else:
                rabs.append(rab)
                a = input("esche?")
            finally:
                print()

    c=int(input("year do"))
    for rab in rabs:
        if rab.year_begin > c:
            print(rab)
esche()








