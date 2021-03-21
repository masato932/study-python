# def test(a=5, b=1, c=2):
#     print(a)
#     print(b)
#     print(c)

# print(test())

# def test(a, b, c, d=20, e=25):
#     print(d)
#     print(e)
#     print(c)
#     print(a)
#     print(b)
    
# test(30, 40, 5, 10, 15)

# def test(a, b, c, d=20, e=25):
#     set_list = [a, b+c, d]
#     return set_list
    
# y = test(5, 10, 15, d=30, e=40)
# print(y)

set_sum = 256

def test(a=1, b=2, c=3, d=4, e=25):
    global set_sum
    # print(set_sum)
    set_sum = a+b+c+d
    # print(set_sum)
    return set_sum

# test()
# print(set_sum)
# test(2,3,4,5,6)
# print(set_sum)
x = test(3,4,5,6,7)
# print(x)
# print(set_sum)
y = test()
# print(set_sum)
# test(4,5,6,7,8)
# print(set_sum)
z = x + y
print(z)
y = y + 1
print(y)