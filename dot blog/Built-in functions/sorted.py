# x = [5, 8, 4, 1, 3, 2, 7, 6]
# y = sorted(x)
# print(y)

# x = [5, 8, 4, 1, 3, 2, 7, 6]
# y = sorted(x, reverse=True)
# print(y)

# x = (5, 8, 4, 1, 3, 2, 7, 6)
# y = sorted(x, reverse=True)
# print(y)

# x = {'b':20, 'c':30, 'a':9, 'd':10}
# y = sorted(x, reverse=True)
# print(y)

# x = {'b':20, 'c':20, 'a':40, 'd':10}
# y = sorted(x.values(), reverse=True)
# print(y)

# x = {'b':20, 'c':30, 'a':40, 'd':10}
# y = sorted(x.items(), reverse=True)
# print(y)

# x = 'cbazdtRMLNKII'
# y = sorted(x, reverse=True)
# print(y)

# x = ['apple', 'Apple', 'amazon', 'Amazon', 'windows', 'Windows', 'walmart', 'Walmart']
# y = sorted(x, reverse=True)
# print(y)

x = ['apple', 'Apple', 'amazon', 'Amazon', 'windows', 'Windows', 'walmart', 'Walmart']
y = sorted(x, key=len, reverse=True)
print(y)