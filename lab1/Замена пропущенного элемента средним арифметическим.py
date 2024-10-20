numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_copy = []
for number in numbers:
    if number is not None:
        numbers_copy.append(number)
numbers[numbers.index(None)] = sum(numbers_copy) / len(numbers)

print("Измененный список: ", *numbers)
