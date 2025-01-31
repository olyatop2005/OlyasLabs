import doctest


class Human:
    """
    Класс человека
    """

    def __init__(self, name: str, surname: str, age: int = None):
        """
        Создание объекта класса "Human":
        :param name: Имя человека
        :type name: str
        :param surname: Фамилия человека
        :type surname: str
        :param age: Возраст человека в годах
        :type age: int

        Пример создания:
        >>> human = Human("Ivan", "Ivanov", 19)
        """

        # Проверки имени
        if not (isinstance(name, str)): raise TypeError("Имя введено не корректно")
        if not (name.isalpha()): raise ValueError("Имя может содержать только буквы")
        if name[0].islower(): raise ValueError("Имя должно начинаться с большой буквы")

        # Проверки фамилии
        if not (isinstance(surname, str)): raise TypeError("Фамилия введена не корректно")
        if not (surname.isalpha()): raise ValueError("Фамилия может содержать только буквы")
        if surname[0].islower(): raise ValueError("Фамилия должна начинаться с большой буквы")

        # Проверки возраста
        if not (isinstance(age, int)): raise TypeError("Возраст может быть только целочисленным")
        if age < 0: raise ValueError("Возраст не может быть отрицательным")
        if age > 150: raise ValueError("Люди столько не живут")

        self.name = name
        self.surname = surname
        self.age = age

    def get_fullname(self) -> str:
        """
        Возвращает фамилию и имя

        :return: str

        Пример:
        >>> human = Human("Ivan", "Ivanov", 19)
        >>> print(human.get_fullname())
        Ivanov Ivan
        """
        return f"{self.surname} {self.name}"

    def get_mood(self) -> str:
        """
        Возвращает фамилию, имя и настроение человека

        :return: str

        Пример:
        >>> human = Human("Ivan", "Ivanov", 19)
        >>> print(human.get_mood())
        Ivanov Ivan happy
        """
        return self.get_fullname() + " happy"

    def __str__(self) -> str:
        """
        Метод возвращает полную информацию об объекте

        Пример:
        >>> human = Human("Ivan", "Ivanov", 19)
        >>> print(human)
        Имя: Ivan, Фамилия: Ivanov, возраст: 19 лет
        """

        return f"Имя: {self.name}, Фамилия: {self.surname}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Метод возвращает строку валидного кода создания данного объекта класса

        Пример:
        >>> human = Human("Ivan", "Ivanov", 19)
        >>> print(human.__repr__())
        Human('Ivan', 'Ivanov', 19)
        """

        return f"Human({self.name!r}, {self.surname!r}, {self.age!r})"


class Student(Human):
    """
    Класс студента
    """

    def __init__(self, name: str, surname: str, age: int, number_of_debts: int = 0):
        """
        Создание объекта класса "Student":
        :param name: Имя человека
        :type name: str
        :param surname: Фамилия человека
        :type surname: str
        :param age: Возраст человека в годах
        :type age: int

        Примеры:
        >>> student = Student("Ivan", "Ivanov", 19, 10)    # Инициализация объекта класса
        """

        # Проверки долгов
        if not (isinstance(number_of_debts, int)): raise TypeError("Количество долгов может быть только целочисленным")
        if number_of_debts < 0: raise ValueError("Количество долгов не может быть отрицательным")
        if number_of_debts > 15: raise ValueError("Студенты с 15+ долгами перестают быть студентами")

        super().__init__(name, surname, age)
        self.number_of_debts = number_of_debts

    def get_mood(self) -> str:
        """
        Возвращает фамилию, имя и настроение человека
        Перегрузка необходима потому что у студента другое настроение во время пересдачи

        :return: str

        Пример:
        >>> student = Student("Ivan", "Ivanov", 19)
        >>> print(student.get_mood())
        Ivanov Ivan sad
        """
        return self.get_fullname() + " sad"

    def __str__(self) -> str:
        """
        Метод возвращает полную информацию об объекте

        Примеры:
        >>> student = Student("Ivan", "Ivanov", 19, 10)
        >>> print(student)
        Имя: Ivan, Фамилия: Ivanov, возраст: 19 лет, Количество долгов: 10
        """

        return super().__str__() + f", Количество долгов: {self.number_of_debts}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку валидного кода создания данного объекта класса

        Примеры:
        >>> student = Student("Ivan", "Ivanov", 19, 10)
        >>> print(student.__repr__())
        Student('Ivan', 'Ivanov', 19, 10)
        """
        return f"Student({self.name!r}, {self.surname!r}, {self.age!r}, {self.number_of_debts!r})"


if __name__ == "__main__":
    doctest.testmod()
