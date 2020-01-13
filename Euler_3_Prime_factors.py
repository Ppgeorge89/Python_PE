import time
import sys
import time


def main():
    start_time = time.time()

    def biggest_prime_factor(num):
        try:
            i = 2
            while i * i < num:
                while num % i == 0:
                    num = num / i
                i = i + 1

            return num
        except TypeError:
            print("You did not insert a valid number...")
            sys.exit()
        except UnboundLocalError:
            print("You did not insert a valid number...")
            sys.exit()

    print(biggest_prime_factor(600851475143))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()