print('test1', end='')
print('test2', end='')

import time

for i in range(10):
    print('\rNo, %d' % i, end='')
    time.sleep(0.5)

import time

pro_size = 10
for i in range(1, pro_size + 1):
    pro_bar = ('=' * i) + (' ' * (pro_size - i))
    print('\r[{0}] {1}%'.format(pro_bar, i / pro_size * 100.), end='')
    time.sleep(0.5)

import time

pro_size = 10
for i in range(1, pro_size + 1):
    pro_bar = ('=' * i) + (' ' * (pro_size - i))
    print('\r[{0}] {1}/{2}'.format(pro_bar, i, pro_size), end='')
    time.sleep(0.5)