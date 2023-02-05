cost = 0
free = 0
partly = 990
full = 1390
age_list = []
tickets = (int(input('Введите количество билетов, которое хотите приобрести\n')))
for i in range(1, tickets+1):
    age = int(input(f'Билет {i}. Введите возраст: \n'))
    age_list.append(age)
    if age < 18:
        cost += free
    elif 18 <= age <= 25:
        cost += partly
    else:
        cost += full

if tickets > 3:
    discount_cost = int(cost * 0.9)
    print('Стоимость билетов со скидкой: ', discount_cost, 'рублей')
else:
    print("Стоимость билетов составляет: ", cost, "рублей")
