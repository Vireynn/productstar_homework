""" Скрипт принимает числа и разбивает их на элементы списка, переводит их в целочисленный тип,
сортирует список и выводит его на экран"""

print('Enter some numbers in one line')  # пропущена кавычка
raw_input = input()
splitted_input = raw_input.split()
parsed_input = list()
for raw in splitted_input:
    parsed_input.append(int(raw))  # ошибка в названии переменной
parsed_input.sort()
print(f'your result: {parsed_input}')  # должна быть функция print вместо int, и ошибка в организации f-строки
