from My_module import Timer
from My_module import Toolkit
import sys


@Timer.timeit
def main():
    def Prime_pair_sets(primes, p):
        flag = True
        for i in primes:
            if p == i:
                flag = False
            elif not Toolkit.prime_or_not(int(str(i) + str(p))) or not Toolkit.prime_or_not(int(str(p) + str(i))):
                flag = False
                break
        return flag

    potential_set = [3, 7, 109, 673]
    for p in Toolkit.SieveOfEratosthenes(10 ** 7):
        if Prime_pair_sets(potential_set, p):
            potential_set.append(p)
            print(potential_set)
            break


if __name__ == '__main__':
    main()
