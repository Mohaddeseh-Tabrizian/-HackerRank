from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title:" + ' ' + str(title))
        print("Author:" + ' ' + str(author))
        print("Price:" + ' ' + str(price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
