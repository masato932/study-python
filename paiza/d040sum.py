# coding: utf-8

list = []
for i in range(7):
    i = int(input())
    list.append(i)
# print(list)

n = sum(x<=30 for x in list)
print(n)