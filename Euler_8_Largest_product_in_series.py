import time
import sys



def main():
    try:
        start_time = time.time()
        filename = "1000_digit_number.txt"
        file = open(filename, "r")
        text = file.read()
        number = list(text)
        str_digit_number = []
        for i in number:
            if i != "\n":
                str_digit_number.append(i)
        final_lst = list(map(int, str_digit_number))
        teamed_num = []
        for i in range(0, 15):
            for j in range(i, 1000 - 12):
                teamed_num.append(final_lst[j:j + 13])
        prod = []
        for i in range(len(teamed_num)):
            tem = 1
            for j in range(len(teamed_num[i])):
                tem *= teamed_num[i][j]
            prod.append(tem)
        print(list(reversed(sorted(prod)))[1])
        file.close()
    except TypeError:
            print("You did not insert a valid number...")
            sys.exit()
    except UnboundLocalError:
            print("You did not insert a valid number...")
            sys.exit()









    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
     main()