st_name = ['大川', '城山', '佐々木', '都築', '野本']
st_value = [95, 87, 76, 89, 92]

for name, value in zip(st_name, st_value):
    x = '氏名：{0} 点数：{1}点'.format(name, value)
    print(x)
print(type(x))

st_no = [1, 2, 5, 8, 10]
st_value = [95, 87, 76, 89, 92]

for no, value in zip(st_no, st_value):
    y = 'No,：{0} 点数：{1}点'.format(no, value)
    print(y)
print(type(y))

st_name = ['大川', '城山', '佐々木', '都築', '野本']
st_value = [95, 87, 76, 89, 92]

tu = list(zip(st_name, st_value))
print(tu)
print(type(tu))