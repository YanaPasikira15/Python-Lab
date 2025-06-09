# Завдання 1:
print("Завдання 1: Площа трьох прямокутників")
areas = []
for i in range(1, 4):
    a = float(input(f"Введіть довжину сторони a прямокутника {i}: "))
    b = float(input(f"Введіть довжину сторони b прямокутника {i}: "))
    area = a * b
    areas.append(area)
    print(f"Площа прямокутника {i}: {area}")
print()

# Завдання 2:
print("Завдання 2: Порівняння гіпотенуз")

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Введіть перший катет першого трикутника: "))
b1 = float(input("Введіть другий катет першого трикутника: "))
a2 = float(input("Введіть перший катет другого трикутника: "))
b2 = float(input("Введіть другий катет другого трикутника: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза першого трикутника: {h1}")
print(f"Гіпотенуза другого трикутника: {h2}")

if h1 > h2:
    print("Перша гіпотенуза більша.")
elif h2 > h1:
    print("Друга гіпотенуза більша.")
else:
    print("Гіпотенузи рівні.")
print()

# Завдання 3:
print("Завдання 3: Перевірка, скільки точок лежить всередині кола")

def is_inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r**2

a = float(input("Введіть координату a (центр кола по x): "))
b = float(input("Введіть координату b (центр кола по y): "))
r = float(input("Введіть радіус R кола: "))

p1, p2 = map(float, input("Введіть координати точки P (p1 p2): ").split())
f1, f2 = map(float, input("Введіть координати точки F (f1 f2): ").split())
l1, l2 = map(float, input("Введіть координати точки L (l1 l2): ").split())

points = [(p1, p2), (f1, f2), (l1, l2)]
count_inside = sum(is_inside_circle(x, y, a, b, r) for x, y in points)
print(f"Кількість точок всередині кола: {count_inside}")
print()

# Завдання 4:
print("Завдання 4: Площа чотирикутника")
X = float(input("Введіть сторону X: "))
Y = float(input("Введіть сторону Y: "))
Z = float(input("Введіть сторону Z: "))
T = float(input("Введіть сторону T: "))

area1 = (X * Y) / 2

s = (Z + T + math.hypot(X - Y, 0)) / 2
area2 = math.sqrt(s * (s - Z) * (s - T) * (s - math.hypot(X - Y, 0)))

total_area = area1 + area2
print(f"Площа чотирикутника: {total_area}")
print()

# Завдання 5:
print("Завдання 5: Натуральні числа, що діляться на кожне із заданих")

n = int(input("Введіть максимальне число n: "))
numbers = list(map(int, input("Введіть дільники через пробіл: ").split()))

def is_divisible(num, divisors):
    return all(num % d == 0 for d in divisors if d != 0)

result = [i for i in range(1, n+1) if is_divisible(i, numbers)]
print("Числа, що діляться на кожне з введених:")
print(result)
