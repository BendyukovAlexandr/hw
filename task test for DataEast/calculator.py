
class Calc:

    def __init__(self):
        self.formula = ""


    def input(self):
        self.virazhenie = input("ваше выражение: {0}".format(self.formula))
        self.logica(self.virazhenie)


    def logica(self, operation):
        if "^" in operation:
            self.formula+=operation
            stepen=list(self.formula)
            for n,i in enumerate(stepen):
                if i=="^":
                    stepen[n]="**"
            self.formula="".join(stepen)
            self.formula = str(eval(self.formula))
        elif operation == "del":
            self.formula = ""
        elif operation == "sqrt":
            self.formula = str((eval(self.formula)) ** 0.5)
        else:
            self.formula += self.virazhenie
            self.formula = str(eval(self.formula))
        print(self.formula)
        self.update()

    def update(self):
        if self.formula=="0":
            self.formula=""
calc=Calc()
print(
"""{blue}
Доступные операции: 
del- удаление предыдущих значений
^-возведение в степень
sqrt-квадратный корень
А так же сложение, вычитание, деление, умножение.
Работает приоритет скобок.
Просьба использовать квадратный корень и очистку предыдущих значений с пустой строкой ввода
{endc}""".format(blue='\033[3m', endc='\033[0m')
)
print()
while True:
    calc.input()