import time
import sys


def main():
    start_time = time.time()

    try:
        def eratosthenes_find_the_prime(n):
                prime_numbers = [2]
                num_1 = 3
                while len(prime_numbers) < n:

                    flag = True
                    for i in prime_numbers:
                        if num_1 % i == 0:
                            flag = False
                            break
                    if flag:
                        prime_numbers.append(num_1)
                    num_1 += 2


                return prime_numbers[-1]
        print(eratosthenes_find_the_prime(10001))

    except TypeError:
            print("You did not insert a valid number...")
            sys.exit()
    except UnboundLocalError:
            print("You did not insert a valid number...")
            sys.exit()

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()