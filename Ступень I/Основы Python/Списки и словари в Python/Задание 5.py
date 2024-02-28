# Словарь из двух списков
# Создайте словарь из двух списков. Чтобы по каждому имени можно было узнать профессию. Выведи профессию maria.

names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']

occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder',
               'developer', 'ml engineer', 'product manager', 'cmo']

dict_ = dict(zip(names, occupations))
print(dict_['maria'])
