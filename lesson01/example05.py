revenue = int(input("Введите значение выручки за прошлый год:"))
costs = int(input("Введите значение издержек за прошлый год:"))

print(revenue-costs)
if revenue > costs:
    print("Ваша фирма получила прибыль")
else:
    print("Ваша фирма в убытке")

staff = int(input("Введите среднесписочную численность сотрудников в прошлом году:"))
print(revenue / staff)