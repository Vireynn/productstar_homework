# List comprehensions
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков. Список должен содержать только
# уникальные значения и быть отсортирован по возрастанию. Вывод через запятую без кавычек.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]

common_list = a + b
result_list = sorted(set([elem for elem in common_list if elem in a and elem in b]))
print(result_list)