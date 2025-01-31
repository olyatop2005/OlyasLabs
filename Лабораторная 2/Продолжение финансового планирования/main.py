from math import ceil

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_shortage = 0

for month in range(months):
    shortage = max(0, spend - salary)
    total_shortage += shortage

    spend *= (1 + increase)

# Результат
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {ceil(total_shortage)}")
