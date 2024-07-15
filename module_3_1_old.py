# Пространство имен и способы вызова функции

def test_():
    a = 11
    b = 45
    print(a, b)


test_()


def test_2(a, b, c):
    print(a, b, c)


test_2(4, 34, 78)

d = 1

print('----------')


def test_function():
    d = 10

    def inner_function():
        d = 'local'
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
