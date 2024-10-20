available_memory_in_mb = 1.44
available_memory_total = available_memory_in_mb * 1024 * 1024

char_cost = 4
chars_in_line = 25
lines_on_page = 50
pages_count = 100

needs_memory_for_book = pages_count * lines_on_page * chars_in_line * char_cost
available_count_of_books = int(available_memory_total // needs_memory_for_book)

print("Количество книг, помещающихся на дискету:", available_count_of_books)
