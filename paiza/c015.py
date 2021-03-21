# coding: utf-8

mylist = []
i = int(input())
for x in range(i):
    x = input()
    mylist.append(x)
# print(mylist)

a = mylist[0].split()
if a[0] in "3":
    y = int(a[1])* 3 // 100
    print(y)
elif a[0] in "5":
    y = int(a[1])* 5 // 100
    print(y)
else:
    y = int(a[1]) // 100
    print(y)