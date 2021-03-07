# nums = (4,8,9,17,33,68,56)
# nums_2xlist = []

# for i in nums:
#     nums_2xlist.append(i ** 2)
    
# print(nums_2xlist)

# nums = (4,8,9,17,33,68,56)
# nums_2xlist = [i ** 2 for i in nums]
    
# print(nums_2xlist)

# nums = (4,6,9,17,33,67,56)
# nums_2xlist = []

# for i in nums:
#     if i % 2 == 0:
#         nums_2xlist.append(i)
    
# print(nums_2xlist)

# nums = (4,8,9,17,33,68,56)
# nums_3xlist = [i for i in nums if i % 3 == 0]
    
# print(nums_3xlist)

nums1 = (4,8,9,17,33,68,56)
nums2 = (3,7,10)
nums_multipl_list = []

for n1 in nums1:
    element_list = []
    for n2 in nums2:
        element_list.append(n1 * n2)
    nums_multipl_list.append(element_list)
    
print(nums_multipl_list)

nums1 = (4,8,9,17,33,68,56)
nums2 = (3,7,10)
nums_multipl_list = [[n2 * n1 for n1 in nums1] for n2 in nums2]
    
print(nums_multipl_list)