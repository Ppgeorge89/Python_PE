import time
import  sys


def main():
    start_time = time.time()

    try:
        sum = 0
        for i in range(0,1000):
            if i % 5 == 0 or i % 3 == 0:
                sum += i
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