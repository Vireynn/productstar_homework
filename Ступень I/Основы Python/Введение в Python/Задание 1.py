def sum(*args):
    """ Суммирует все аргументы функции """
    result = 0
    for elem in args:
        result += elem
    return result

# Принимаем 4 числа
numbers = [int(input(f'num{x}: ')) for x in range(4)]

# Вывод суммы принятых чисел
print(f"Result: {sum(*numbers)}")
