import time
import sys

def main():
    start_time = time.time()
    try:
        def number_decomposition(num):
            str_num = str(num)
            digits = []
            for i in range(0, len(str_num)):
                digits.append(int(str_num[i]))
            return digits

        def palindromic_number(num):
            digits = number_decomposition(num)
            if digits == list(reversed(digits)):
                return True
            else:
                return False


        palindromic_numbers = []
        for i in range(100, 1000):
            for j in range(100, 1000):
                if palindromic_number(i * j):
                    palindromic_numbers.append(i * j)

        print(list(reversed(sorted(palindromic_numbers)))[0])

    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()
    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
