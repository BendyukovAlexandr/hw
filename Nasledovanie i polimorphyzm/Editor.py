# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.

class Editor():
    def __init__(self, document):
        self.document=document

    def view_documents(self):
        print(self.document)

    def edit_document(self):
        print("free version, please upgrade to Pro Editor")


class ProEditor(Editor):
    def edit_document(self):
        while True:
            x=input("please, enter password: ")
            if x=="1234":
                print("Pro Editor opened")
            elif x=="exit":
                print("exit")
                break
            else:
                print("incorrect password")
