# версия до обновления


def test(codes, *types, region='Санкт-Петербург', **values):
    # Функция с произвольным числом параметров разного типа
    for key, value in values.items():
        print(key, value)
    print(types)


test('автомобильные номера', 98, 178, 198, region='Санкт-Петербург', code='98',
     region_code='Санкт-Петербург - 98')
