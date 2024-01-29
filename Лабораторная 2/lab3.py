class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def author(self):
        return self.author

    def name(self):
        return self.name

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        Book.__init__(self, name, author)
        self.__pages = pages
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.__pages!r})"
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if 0 < pages :
            self.__pages = pages
        else:
            print("Недопустимая длительность")

    @property
    def pages(self):
        return self.__pages



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        Book.__init__(self, name, author)
        self.__duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.__duration})"
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if 0 < duration :
            self.__duration = duration
        else:
            print("Недопустимая длительность")

    @property
    def duration(self):
        return self.__duration



print(PaperBook("name1", "author1", 99).__repr__())
