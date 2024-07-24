print('Функция с произвольным числом параметров разного типа')
# Создайте новую функцию def test... с произвольным числом
# параметров разного типа, функция должна распечатывать эти
# параметры внутри своего тела


def test(codes, *types, region='Санкт-Петербург', **values):
    for key, value in values.items():
        print(key, value)
    print(types)


test('автомобильные номера', 98, 178, 198, region='Санкт-Петербург', code='98',
     region_code='Санкт-Петербург - 98')

print('\nРекурсивная функция - факториал числа n')
# Создайте рекурсивную функцию, которая будет считать факториал
# от числа n, n - передается в параметре


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


print('\nРекурсивная функция - факториал числа n + input')
n = int(input("Введите число: "))


def factorial_(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))
