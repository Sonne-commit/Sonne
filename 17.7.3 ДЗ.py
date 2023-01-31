per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты:\n '))
print('Вы вложили:  ',money)
deposit = []
for bank in per_cent:
    profit = money * per_cent[bank]/100
    deposit.append(profit)

print('По всем предложениям: ', deposit)
print('Лучшее предложение: ', max(deposit))