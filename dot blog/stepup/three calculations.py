# num = 3

# if num % 2 == 0:
#     x = '偶数'
# else:
#     x = '奇数'

# print(x)

# num = 4

# x = '偶数' if num % 2 == 0 else '奇数'

# print(x)
nums = [2, 5, 8, 9, 11]

for num in nums:
    if num % 2 == 0:
        x = '偶数'
    else:
        x = '奇数'
    print(type(x))
    print(x)

nums = [2, 5, 8, 9, 11]

x = ('偶数' if num % 2 == 0 else '奇数' for num in nums)

print(type(x))

for result in x:
    print(result)

# nums = [2, 5, 8, 9, 11]

# x = map(lambda num:'偶数' if num % 2 == 0 else '奇数', nums)

# for result in x:
#     print(result)