from task_1 import Cat, Student, Teacher

if __name__ == "__main__":
    student = Student("Bogdan", 8)
    teacher = Teacher("Zelikman", 1)

    try:
        cat = Cat(-1, "british")
    except Exception:
        print('Ошибка: неправильные данные')

    try:
        student.pass_session()
    except Exception:
        print('Ошибка: неправильные данные')

    try:
        teacher.add_data(1)
    except Exception:
        print('Ошибка: неправильные данные')
