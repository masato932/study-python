# st_name = ['大川', '城山', '佐々木', '都築', '野本']

# for i in range(len(st_name)):
#     print('No,：{0} 氏名：{1}'.format(i, st_name[i]))

st_name = ['大川', '城山', '佐々木', '都築', '野本']

for i, name in enumerate(st_name, 2):
    i = i * 7 / 10 - 1
    print('No,：{0} 氏名：{1}'.format(i, name))