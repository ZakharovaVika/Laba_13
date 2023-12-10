#3 Определить суммарную стоимость билетов женщин на борту в возрастном интервале медиана ± 5 лет

import csv
filename = open('Titanic.csv', 'r')
file = csv.DictReader(filename)
def median(age):
    n = len(age)
    index = n // 2
    if n % 2:
        return sorted(age)[index]
    return sum(sorted(age)[index - 1:index + 1]) / 2


age = []
total = []
for col in file:
    if col['sex'] == 'female':
        if col['age'] != '':
            age.append(col['age'])
            data = {
                'age': col['age'],
                'class': col['class']
            }
            total.append(data)
res = int(median(age))
money = 0
for i in total:
    if res - 5 <= float(i['age']) <= res + 5:
        if i['class'] == 'First':
            money += 150
        if i['class'] == 'Second':
            money += 60
        else:
            money += 30
print(f'Cуммарная стоимость билетов женщин на борту '
      f'в возрастном интервале медиана ± 5 лет составила : {money}$.')





