# Считаем слова в строке
# Дана строка. Выведите слово, которое встречается чаще всего. Если таких слов несколько, выведите то, которое меньше
# в лексикографическом порядке.

s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star kafka ' \
    'stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit predict ' \
    'analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course stack flow ' \
    'dict list python stack course '

split_str = s.split()
counter = dict.fromkeys(split_str, 0)

for word in split_str:
    counter[word] += 1

print(max(counter, key=counter.get))
