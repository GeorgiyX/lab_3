# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
def print_result(foo):
    def print_foo():
        print(foo.__name__)
        returned = foo()
        if type(returned) == list:
            for ret in returned:
                print(ret)
        elif type(returned) == dict:
            for key, value in dict(returned).items():
                print(str(key) + str(' = ') + str(value))
        else:
            print(returned)
    return print_foo
