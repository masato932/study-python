# from random import randrange

# x = randrange(0, 10, 1)
# while x <= 5:
#     print(x)
#     x = randrange(0, 10, 1)

from random import randrange

x = randrange(0, 10, 1)
flag = True
while flag:
    print(x)
    if x > 3:
        break
    else:
        x = randrange(0, 10, 1)