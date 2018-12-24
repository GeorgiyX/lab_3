#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': None, 'price': 800, 'color': 'white'},
    {'title': None, 'price': None, 'color': None}
]

# Реализация задания 1
# print(list(field(goods, 'title')))
# print(list(field(goods, 'title', 'price')))
# print(list(gen_random(1,10,10)))
ret = field(goods, 'title', 'price')
print(type(ret))
for i in ret:
    print(type(i))
    print(i)