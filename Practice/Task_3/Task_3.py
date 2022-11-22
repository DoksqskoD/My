# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.

import random
import numpy

Dict={}

for w in numpy.array([random.randint(0,100) for i in range(100)]):
    for z in numpy.array([random.randint(0,100) for i in range(100)]):
        Dict.update({str(w):str(z)})
print(Dict)