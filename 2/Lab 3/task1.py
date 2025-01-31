class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int): raise TypeError
        if pages < 0: raise ValueError
        super().__init__(name, author)

        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int): raise TypeError
        if value < 0: raise ValueError

        self._pages = value

    def __str__(self):
        return super().__str__() + f", количество страниц {self._pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if not (isinstance(duration, int) or isinstance(duration, float)): raise TypeError
        if duration < 0: raise ValueError
        super().__init__(name, author)

        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if not (isinstance(value, int) or isinstance(value, float)): raise TypeError
        if value < 0: raise ValueError

        self._duration = value

    def __str__(self):
        return super().__str__() + f", длительность {self._duration}"


# блоки проверки того, что написал

a = AudioBook("asd", "koio", 1)
print(str(a))
