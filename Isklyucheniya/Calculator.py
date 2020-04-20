# Напишите программу-калькулятор, которая поддерживает следующие операции:
# сложение, вычитание, умножение, деление и возведение в степень.
# Программа должна выдавать сообщения об ошибке и продолжать работу
# при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень.
def calculator():

    while True:

        x=input("первое число ")

        if x=="exit":
            break
        else:
            y=input("операция ")
            z=int(input("второе число "))

            x=int(x)
            if y=="/":
                print(x/z)
            if y=="*":
                print(x*z)
            if y=="+":
                print(x+z)
            if y=="-":
                print(x-z)
            if y == "**":
                print(x**z)



def oshibki():
    try:
        calculator()
    except ZeroDivisionError:
        print("division by zero")
        oshibki()

oshibki()



