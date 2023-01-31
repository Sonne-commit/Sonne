per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
mone = int(input('Введите сумму, которую планируете положить под проценты:\n '))
print('Вы вложили:  ',mone)
deposit = []
for bank in per_cent:
    percent = mone * per_cent[bank]/100
    deposit.append(percent)

print('По всем предложениям: ', deposit)
print('Лучшее предложение: ', max(deposit))