# nums = (4,8,9,17,33,68,56)
# nums_2xset = {i ** 2 for i in nums}
    
# print(nums_2xset)

nums = (4,8,9,17,33,68,56)
nums_even_set = set()

for i in nums:
    if i % 2 == 0:
        nums_even_set.add(i)
    
print(nums_even_set)

nums = (4,8,9,17,33,68,56)
nums_even_set = {i for i in nums if i % 3 == 0}
    
print(nums_even_set)