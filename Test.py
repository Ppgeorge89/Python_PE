from My_module import Timer
from My_module import Toolkit
from operator import xor
import string
from itertools import product
import math


@Timer.timeit
def main():
    sum = (97.5/100)**25
    print(sum)


if __name__ == '__main__':
    main()
