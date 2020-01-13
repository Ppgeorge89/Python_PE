import time
import sys
import math


def main():
    try:
        start_time = time.time()



        prime = [True for i in range(2*10**6 + 1)]
        p = 2
        while (p * p <= 2*10**6):
            if (prime[p] == True):
                for i in range(p * 2, 2*10**6 + 1, p):
                    prime[i] = False
            p += 1

        sum = 0
        for p in range(2, 2* 10 **6):
            if prime[p]:
                print(p)
                sum += p
        print(sum)




        print("--- %s seconds ---" % (time.time() - start_time))
    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()
    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()

if __name__ == '__main__':
     main()