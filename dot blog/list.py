# x = ['a', 'b', 'c', 'd']
# print(type(x))
# print(x)
  # 
# x = [10, 10.5, False, 'a']
# print(type(x))
# print(x)

# x = ['a', 'b', 'c', 'd']
# y = ['e', 'f', 'g', 'h']
# z = [x, y]
# print(z)

# x = ['a', 'b', 'c', 'd']
# y = ['e', 'f', 'g', 'h']
# z = x + y * 3
# print(z)

# x = []
# x += ['a', 'b', 'c', 'd']
# x += ['e', 'f', 'g', 'h']
# x += ['i', 'j', 'k', 'l']
# print(x)

# x = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
# y = x[1][-2:]
# print(y)

x = ['a', 'b', 'c', 'd']
x[1] = 'z'
del x[2]
print(x)