# x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
# print(x)

# x = {'A':10, 'B':10.5, 'C':False, 'D':'a'}
# print(type(x))
# print(x)

# x = {'A':[95, 68, 76, 98, 82], 'B':[86, 72, 91, 88, 73], 'C':[76, 77, 89, 99, 71]}
# print(type(x))
# print(x)

# a_key = 'A'
# a_value = [95, 68, 76, 98, 82]
# b_key = 'B'
# b_value = [86, 72, 91, 88, 73]
# c_key = 'C'
# c_value = [76, 77, 89, 99, 71]
# d_key = 'D'
# d_value = [12, 34, 56, 78, 90]
# x = {a_key:a_value, b_key:b_value, c_key:c_value, d_key:d_value}
# # print(type(x))
# # z = x[a_key]
# x["B"] = "z"
# del x["C"]
# print(x)

x = {}
x['A'] = [95, 68, 76, 98, 82]
x['B'] = [86, 72, 91, 88, 73]
x['C'] = [76, 77, 89, 99, 71]
x['D'] = [3, 2, 5, 6, 7]
print(type(x))
del x["B"]
print(x)
