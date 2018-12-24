import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(mass, *keysmass):
    if len(keysmass) > 1:
        for diction in mass:
            dictionForPrint = {}
            for key, value in dict(diction).items():
                if key in keysmass and value != None:
                    dictionForPrint[key] = value
            if len(dictionForPrint) !=0:
                yield dictionForPrint
    elif len(keysmass) == 1:
        for diction in mass:
            for key, value in dict(diction).items():
                if key in keysmass and value != None:
                    yield str(value)
    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)
