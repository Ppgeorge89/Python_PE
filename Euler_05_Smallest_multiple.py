import time
import sys
from math import gcd
from functools import reduce


def main():
    start_time = time.time()

    try:
        def lcm(*numbers):
            def lcm(a, b):
                return (a * b) // gcd(a, b)

            return reduce(lcm, numbers, 1)


        lst = [x for x in range(1,21)]
        for i in range(20, 0, -1 ):
            for j in range(1, i):
                if i % j == 0 and j in lst:
                    lst.remove(j)
        print(lcm(11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()
    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
