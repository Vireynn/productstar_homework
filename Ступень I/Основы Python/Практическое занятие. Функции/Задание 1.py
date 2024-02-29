from typing import List, Dict

fake_db = [{'name': 'Maxim', 'age': 23, 'gender': 'male'},
           {'name': 'Anna', 'age': 22, 'gender': 'female'},
           {'name': 'Herman', 'age': 23, 'gender': 'male'},
           {'name': 'Ivan', 'age': 19, 'gender': 'male'},
           {'name': 'Vladimir', 'age': 71, 'gender': 'male'},
           {'name': 'Vlada', 'age': 22, 'gender': 'female'},
           {'name': 'Tanya', 'age': 35, 'gender': 'female'},
           {'name': 'Karina', 'age': 38, 'gender': 'female'},
           {'name': 'Nikita', 'age': 22, 'gender': 'attack_helicopter'},
           {'name': 'Irina', 'age': 45, 'gender': 'female'}
           ]

def average_age(db: List[Dict], gender: str) -> float:
    """ Функция возвращает средний возраст людей заданного пола. """
    ages = [person['age'] for person in db if person['gender'] == gender]
    return sum(ages)/len(ages)

print(average_age(fake_db, 'female'))



