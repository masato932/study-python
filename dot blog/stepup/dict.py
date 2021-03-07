# keys = ['a', 'b', 'c']
# dicts = {key:'1' for key in keys}
    
# print(dicts)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dicts = {}

for key, value in zip(keys, values):
    dicts[key] = value
    
print(dicts)

keys = ['a', 'b', 'c']
values = [1, 2, 4]

dicts = {key:value for key, value in zip(keys, values)}
    
print(dicts)