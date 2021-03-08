# x = 'テキスト'
# print(isinstance(x, str))
# x = 5
# print(isinstance(x, int))
# x = 5.7
# print(isinstance(x, float))
# x = True
# print(isinstance(x, bool))
# x = [10, 20, 30, 'テキスト']
# print(isinstance(x, list))
# x = (10, 20, 30, 'テキスト')
# print(isinstance(x, tuple))
# x = {'a':10, 'b':20, 'c':30, 'd':'テキスト'}
# print(isinstance(x, dict))
# x = {10, 25, 40, 65}
# print(isinstance(x, set))
# x = frozenset({10, 25, 40, 65})
# print(isinstance(x, frozenset))
# x = 5 + 2j
# print(isinstance(x, complex))
# x = b'foo'
# print(isinstance(x, bytes))

x = [1,2]

if isinstance(x, str):
    print('テキスト')
elif isinstance(x, int):
    print('整数')
elif isinstance(x, float):
    print('浮動小数点')
else:
    print('etc')