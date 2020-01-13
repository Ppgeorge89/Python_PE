import time
import sys


def main():
    start_time = time.time()
    try:
        f_1 = 1
        f_2 = 2
        f = f_1 + f_2
        sum = 2
        while f <= 4 * 10 ** 6:
            if f % 2 == 0:
                sum += f
            f_1 = f_2
            f_2 = f
            f = f_1 + f_2
    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()
    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()

    print(sum)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
