per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
mone = int(input('Введите сумму, которую планируете положить под проценты '))
deposit = [(keys, round(values / 100 * mone,)) for keys, values in per_cent.items()]
max_deposit = (max(deposit, key=lambda x: x[1]))
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))
