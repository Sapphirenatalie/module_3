# Распаковка параметров и параметры функции
# Функция с параметрами по умолчанию

print('Функция с параметрами по умолчанию:')


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


print('Распаковка параметров')

values_list = [7, False, [3, 8]]
values_dict = {'a': 4, 'b': 5, 'c': 6}

print_params(*values_list)
print_params(**values_dict)

print()

# Распаковка параметров
# отдельные параметры
print('Распаковка + отдельные параметры:')

values_list_2 = ['Санкт-Петербург', 1703]

print_params(*values_list_2, 42)
