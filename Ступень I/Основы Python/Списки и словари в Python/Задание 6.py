# Три в одном
# Напишите код, который соединит эти словари в один:
dict1 = {1: 10, 2: 20, 3901: 11, 384: 13, 8489: 1, 48: 10}
dict2 = {3: 30, 4: 40, 93: 12, 91: 41, 95: 1, 841: 11, 584: 11}
dict3 = {5: 50, 6: 60, 9: 90, 3: 13, 7: 11}

common_dict = dict1 | dict2 | dict3
common_dict_values = list(common_dict.values())

print(f"{len(common_dict)},{max(common_dict_values, key=common_dict_values.count)}")

