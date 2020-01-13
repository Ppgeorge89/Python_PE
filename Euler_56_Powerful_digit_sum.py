from My_module import Timer
from My_module import Toolkit

@Timer.timeit
def main():

    largest = 0
    for a in range(0, 100):
        for b in range(0, 100):
            s = 0
            for i in Toolkit.number_decomposition(a ** b):
                s += i
            if s > largest:
                largest = s
    print(largest)










if __name__ == '__main__':
    main()

