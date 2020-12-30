from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

i = 0
for el in cycle('Привет!'):
    if i > 5:
        break
    print(el)
    i += 1

