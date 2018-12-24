import json
import random
from librip.ctxmngrs import timer
#from librip.decorators import print_result

def print_result(func):
    def print_foo(lst):
        print(func.__name__)
        returned = func(lst)

        if isinstance(returned, list):
            print('\n'.join([str(i) for i in returned]))
        return returned

    return print_foo

path = "data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(*args):
    return sorted(list(set([data[prof]["job-name"].lower() for prof in range(len(data))])))

@print_result
def f2(profs):
    return list(filter(lambda x: str(x).startswith("программист"), profs))

@print_result
def f3(profs):
    return [i + " с опытом Python" for i in profs]

@print_result
def f4(profs):
    money = [random.randint(100000, 200000) for i in range(len(profs))]
    return ["{}, зарплата {} руб.".format(x, y) for x, y in zip(profs, money)]

with timer():
    f4(
        f3(
            f2(
                f1(data))))
