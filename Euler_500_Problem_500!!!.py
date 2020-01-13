from My_module import Timer
from My_module import Toolkit

@Timer.timeit
def main():

    primes = Toolkit.SieveOfEratosthenes(10**7)

    def power_of_primes(p):
        i = 0
        lst = []
        while p ** (2**i) <= 10**7:
            lst.append(p**(2**i))
            i += 1
        return lst




    def A050376_till(n):
        seq = []
        while len(seq) < n:
            for i in primes:
                seq += power_of_primes(i)
        return list(sorted(list(set(seq))))

    final = A050376_till(10**7)[:500500]
    res = 1
    for i in final:
        res *= i
    print(res % 500500507)