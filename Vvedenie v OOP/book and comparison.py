# Создайте класс, описывающий книгу.
# Он должен содержать информацию об авторе, названии, годе издания и жанре.
# Создайте несколько разных книг.
# Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
# Создайте класс, описывающий отзыв к книге.
# Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

import copy

class Book:
    def __init__(self, author, name, date, genre, otzyv=[]):
        self.author=author
        self.name=name
        self.date=date
        self.genre=genre
        self.otzyv=otzyv

    def __eq__(self, other):
        if self.author==other.author and\
    self.name==other.name and\
    self.date==other.date and\
    self.genre==other.genre:
            return True
        else:
            return False

    def __as_string(self, format_string):
        return format_string.format(
            self.author,
            self.name,
            self.date,
            self.genre,
            self.otzyv
        )

    def __str__(self):
        book = self.__as_string('"{1}" by {0} (published in {2}, genre: {3})'
                                '\notzyv:\n')
        otzyv = '\n'.join(map(str, self.otzyv)) or 'No otzyv.'
        return book + otzyv
    def __repr__(self):
        return self.__as_string("{0!r}, {1!r}, {2!r}, {3!r}")


class otzyvy:
    def __init__(self, otzyv):
        self.otzyv=otzyv

def main():
    orwell1984 = Book('George Orwell', '1984', 1949, 'dystopia')
    orwell_copy = copy.copy(orwell1984)
    learning_python = Book('Mark Lutz', 'Learning Python', 2013, 'tutorial')

    orwell1984.otzyv = [
         'Awesome book, changed my perception of the life',
        "Not bad, but Huxley's scenario seems more realistic to me",
    ]

    print(orwell1984)
    print(learning_python)


    print(repr(orwell1984))
    print(repr(learning_python))

    print(orwell1984 == orwell_copy)
    print(orwell1984 != orwell_copy)
    print(orwell1984 == learning_python)
    print(orwell1984 != learning_python)
    print(learning_python == learning_python)
    print(learning_python != learning_python)


if __name__ == '__main__':
    main()
