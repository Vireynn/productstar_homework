questions = {0: {'question': 'Какая версия языка сейчас актуальна?', 'answer': 'Python3'},
             1: {'question': 'Какая кодировка используется в строках?', 'answer': 'UTF8'},
             2: {'question': 'Сколько значений есть у bool?', 'answer': '2'},
             3: {'question': 'Как называется соединение двух строк в одну единую строку?', 'answer': 'Конкатенация'},
             4: {'question': 'Какая функция разделяет строку в случае нахождения разделителя?', 'answer': 'split'},
             5: {'question': 'Какая функция объединяет список из строк в одну строку?', 'answer': 'join'},
             6: {'question': 'Как называется каждый проход цикла?', 'answer': 'Итерация'},
             7: {'question': 'Какое выражение дает возможность выйти из цикла?', 'answer': 'break'},
             8: {'question': 'Какой метод преобразует все символы в строке в нижний регистр?', 'answer': 'lower'},
             9: {'question': 'Какой метод преобразует все символы в строке в верхний регистр?', 'answer': 'upper'}
             }

i = correct_answers = incorrect_answers = 0

while i < 10:
    print(questions[i]['question'])
    answer = input("Ответ: ")
    if answer.lower() == questions[i]['answer'].lower():
        correct_answers += 1
        print(f"Ответ пользователя «{answer}» верен.\n")
        i += 1
    else:
        incorrect_answers += 1
        print("Неверный ответ.\n")

print(f"Количество попыток: {correct_answers + incorrect_answers},\n"
      f"Количество верных ответов: {correct_answers},\n"
      f"Количество неверных ответов: {incorrect_answers}.")
