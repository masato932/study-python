x = [10, 20, 30, 'テキスト']
print(len(x))

x = (10, 20, 30, 'テキスト')
print(len(x))

x = {'a':10, 'b':20, 'c':30, 'd':'テキスト'}
print(len(x))

x = {10, 25, 40, 65}
print(len(x))

x = frozenset({10, 25, 40, 65})
print(len(x))

x = range(4)
print(len(x))
print(x)

x = 'text'
print(len(x))

x = 'text　テキスト text'
print(len(x))

x = '''
text　テキスト text
text　テキスト text
'''
print(len(x))