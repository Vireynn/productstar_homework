# Самая непопулярная буква
# Напишите код, который для любой строки автоматически вернет словарь с количеством вхождений каждого символа. Потом,
# используя этот код, выведи для строки given_string 8 самых непопулярных букв без пробелов и запятых.
# Регистр надо учитывать!

given_string = 'Python Star Course for beginners and experts for data science and analytics without sql with code'

result_dict = dict.fromkeys(given_string, 0)

for letter in given_string:
    result_dict[letter] += 1

unpopular_letters = sorted(list(result_dict.items()), key=lambda x: x[1])[:8]
[print(x, end='') for x in dict(unpopular_letters).keys()]
