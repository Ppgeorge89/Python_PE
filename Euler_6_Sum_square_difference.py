import time
import sys


def main():
    start_time = time.time()

    try:
        squares_1 = 0
        for i in range(1, 101):
            squares_1 += i**2
        temp = 0
        for i in range(1, 101):
            temp += i
        squares_2 = temp ** 2
        print(squares_2 - squares_1)
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