# Функция для поиска первого индекса товара
def find_first_index(items_list, item):
    try:
        # Вернуть индекс первого вхождения товара
        return items_list.index(item)
    except ValueError:
        # Вернуть None, если товар не найден
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Поиск индексов для заданных товаров
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
