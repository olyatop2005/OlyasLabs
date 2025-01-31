import doctest


class Cat:

    def __init__(self, age: int, breed: str, name: str = "Barsik"):
        """
        Создание объекта класса "Cat":

        :param age: Возраст кота
        :type age: int
        :param breed: порода кота
        :type breed: str
        :param name: имя кота
        :type name: str
        """
        self.name = name

        if age >= 0:  # Возраст не может быть отрицательным
            self.age = age
        else:
            raise ValueError("Значение не может быть отрицательным")

        self.breed = breed

    def meow(self) -> None:
        """
        Says MEOW
        """
        print("MEOW")

    def get_data(self) -> tuple[str, int, str]:
        """
        Примеры:
        >>> print(*Cat(Lab 3, "britan").get_data())   # данные объекта
        Barsik Lab 3 britan

        :return: данные кота
        :rtype: str
        """
        return self.name, self.age, self.breed


class Student:
    def __init__(self, surname: str = None, pasted_sessions: int = 0, is_in_university: bool = False):
        """
        Создание объета класса "student"
        :param surname: фамилия студента
        :type surname: str
        :param pasted_sessions: количество сданных сессий
        :type pasted_sessions: int
        :param is_in_university: Учится ли студент в ВУЗе
        :type is_in_university: bool

        Примеры:
        >>> student1 = Student("Ivanov", 1, True)   # Инициализация объекта класса
        """
        self.surname = surname

        if pasted_sessions > 8 or pasted_sessions < 0:
            raise ValueError("Pasted sessions must be lower than 8 and greater than 0")
        self.pasted_sessions = pasted_sessions

        self.is_in_university = is_in_university

    def pass_session(self) -> None:
        """
        Функция для сдачи 1 сессии студентом
        """
        if not self.is_in_university:
            raise Exception("Student not in university can't pass sesseion")

        self.pasted_sessions += 1
        self.is_in_university = self.pasted_sessions > 8

    def get_data(self) -> tuple[str, int, bool]:
        """
        Возвращает данные студента

        :return: tuple[str, int, bool]
        """
        return self.surname, self.pasted_sessions, self.is_in_university


class Teacher:
    def __init__(self, surname: str = None, number_of_students_expelled: int = None):
        """
        Создание объекта класса "prepod"
        :param surname: Фамилия преподавателя
        :param number_of_students_expelled: Количество отчисленных этим преподавателем студентов

        Примеры:
        >>> prepod1 = Teacher("Zelikman", 18634)
        """
        self.surname = surname
        if number_of_students_expelled < 0:
            raise ValueError("Значение не может быть отрицательным")

        self.number_of_students_expelled = number_of_students_expelled

    def add_data(self, number_of_students_expelled: int = None) -> None:
        """
        Функция добавления данных о преподавателе
        :param number_of_students_expelled: Количество отчисленных этим преподавателем студентов
        """
        if number_of_students_expelled >= 0:
            self.number_of_students_expelled = number_of_students_expelled
        else:
            raise ValueError("Значение не может быть отрицательным")

    def print_data(self) -> None:
        """
        Функция вывода данных о преподавателе
        """
        print(self.surname, self.number_of_students_expelled)


if __name__ == "__main__":
    doctest.testmod()
