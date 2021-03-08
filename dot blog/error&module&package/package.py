# from test_pac import test_mod1, test_mod2

# def main():
#     print(test_mod1.add_square2(1, 2))
#     print(test_mod1.add_square5(1, 2))

#     print(test_mod2.text_lower('Python'))
#     print(test_mod2.text_upper('Python'))

# from test_pac import test_mod1 as t_m1
# from test_pac import test_mod2 as t_m2

# def main():
#     print(t_m1.add_square2(1, 2))
#     print(t_m1.add_square5(1, 2))

#     print(t_m2.text_lower('Python'))
#     print(t_m2.text_upper('Python'))

# if __name__ == "__main__":
#     main()

# from test_pac.test_mod1 import add_square2, add_square5
# from test_pac.test_mod2 import text_lower, text_upper

# def main():
# 	print(add_square2(1, 2))
# 	print(add_square5(1, 2))

# 	print(text_lower('Python'))
# 	print(text_upper('Python'))

# if __name__ == "__main__":
#     main()

from test_pac.test_mod1 import *
from test_pac.test_mod2 import *

def main():
    print(add_square2(1, 2))
    print(add_square5(1, 2))

    print(text_lower('Python'))
    print(text_upper('Python'))

if __name__ == "__main__":
    main()