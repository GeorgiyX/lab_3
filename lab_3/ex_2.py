#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data = ['a', 'A', 'b', 'B', 'C', 'c', 'C']
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
unique1 = Unique(data1)
unique2 = Unique(data2)
unique3 = Unique(data, True)
unique4 = Unique(data)
# Реализация задания 2
for i in unique1:
    print(i)
for i in unique2:
    print(i)
for i in unique3:
    print(i)
for i in unique4:
    print(i)
