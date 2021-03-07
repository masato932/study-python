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

def test(a, b, c, d=20, e=25):
    set_list = [a, b+c, d]
    return set_list
    
y = test(5, 10, 15, d=30, e=40)
print(y)

set_sum = 256

def test(a, b, c, d, e=25):
    global set_sum
    print(set_sum)
    set_sum = a+b+c+d
    return set_sum
    
y = test(1, 10, 15, d=70, e=40)
print(y)
print(set_sum)