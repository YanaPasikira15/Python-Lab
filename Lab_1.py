# Завдання 1:
a = float(input("Введіть перше число (ціле або дробове): "))
b = float(input("Введіть друге число (ціле або дробове): "))
c = float(input("Введіть третє число (ціле або дробове): "))
d = float(input("Введіть четверте число (ціле або дробове): "))

# Завдання 2:
sum_result = a + b
sub_result = c - d
mul_result = a * c
div_result = b / d if d != 0 else "Ділення на нуль"
pow_result = a ** 2
int_div_result = int(c) // int(b) if b != 0 else "Цілочисленне ділення на нуль"
mod_result = int(d) % int(a) if a != 0 else "Остача від ділення на нуль"

results = [sum_result, sub_result, mul_result, div_result, pow_result, int_div_result, mod_result]

# Завдання 3:
print("\nКількість елементів у списку результатів:", len(results))
print("Парні елементи списку (тільки числові):")
for item in results:
    if isinstance(item, (int, float)) and item % 2 == 0:
        print(item)

# Завдання 4:
if len(results) >= 5:
    results[1], results[4] = results[4], results[1]
    print("\nСписок після обміну другого і п’ятого елементів:")
    print(results)
else:
    print("Недостатньо елементів для обміну.")

# Завдання 5:
name = input("\nВведіть ваше прізвище та ім’я: ")
print("\nВиконавець лабораторної роботи:")
print(name)
print("Висновки:")
print("Я навчився(-лася) працювати зі змінними, списками та вводом/виводом.")
print("Я зрозумів(-ла), як виконувати базові математичні операції.")
print("Я навчився(-лася) обробляти списки та керувати потоком програми.")
