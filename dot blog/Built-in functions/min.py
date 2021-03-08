# x = [30, 20, 10, 40]
# print(min(x))
# print(max(x))
# x = (30, 20, 10, 40)
# print(min(x))
# x = {'b':20, 'c':30, 'a':10, 'd':40}
# print(min(x))
# x = {'b':20, 'c':30, 'a':10, 'd':40}
# print(min(x.values()))
# print(max(x.values()))
# x = {30, 20, 10, 40, 5}
# print(min(x))

x = range(2, 93, 4)
print(min(x))
print(max(x))

x = 'cbaBCA'
print(min(x))

x = ['apple', 'Apple', 'amazon', 'Amazon', 'windows', 'Windows', 'walmart', 'Walmart']
print(min(x))

x = [30, 20, 10, 40, 30, 20, 10, 40]
print(min(x))

x = ['apple', 'Apple', 'amazon', 'Amazon', 'windows', 'Windows', 'walmart', 'Walmart', "pen"]
print(min(x, key=len))