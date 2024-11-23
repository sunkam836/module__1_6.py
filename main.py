# part 1
my_dict = {'Николай': 1987, 'Василий': 1983, 'Алина': 1971, 'Валентин': 1968}
print(my_dict)
print(my_dict['Николай'])
print(my_dict.get('Алексей', 'Нет такого'))
my_dict.update({'Каролина': 2011, 'Анжелика': 2011})
print(my_dict)
del my_dict['Василий']
print(my_dict)
# part 2
my_set = {1, 3, 5, 4, 3, 2, 8, 4, 1}
print(my_set)
my_set.update({9, 7, 5})
my_set.remove(3)
print(my_set)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
