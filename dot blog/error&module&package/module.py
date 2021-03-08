# import test_mod
# import test_mod as t_m

# from test_mod import add_square2, add_square5

from test_mod import *

def main():
    # print(test_mod.add_square2(1, 2))
    # print(test_mod.add_square5(1, 3))
    print(add_square2(1, 2))
    print(add_square5(1, 3))

    # print(t_m.add_square2(1, 2))
    # print(t_m.add_square5(1, 1))

if __name__ == "__main__":
    main()