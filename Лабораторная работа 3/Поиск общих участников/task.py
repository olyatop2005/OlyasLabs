# Функция для поиска общих участников
def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки участников на списки
    participants_group1 = set(group1.split(delimiter))
    participants_group2 = set(group2.split(delimiter))

    # Находим пересечение множеств
    common_participants = participants_group1 & participants_group2

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Данные участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", common)
