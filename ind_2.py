from prime_test import square_root_test

def ind_2():
    with open('table_ind_1.txt', 'w') as File:
        header = "Число     | "
        for test_num in range(1, 101):
            if test_num < 10:
                header += f"{test_num} тест  | "
            else:
                header += f"{test_num} тест | "
        File.write(f"{header}\n")

        for number in range(2, 100):
            row = ""
            if number < 10:
                row += f"{number}         | "
            elif number < 100:
                row += f"{number}        | "
            elif number < 1000:
                row += f"{number}       | "
            elif number < 10000:
                row += f"{number}      | "
            elif number < 100000:
                row += f"{number}     | "
            elif number < 1000000:
                row += f"{number}    | "
            elif number < 1000000:
                row += f"{number}   | "
            elif number < 1000000:
                row += f"{number}  | "
            else:
                row += f"{number}"

            for iter_count in range(1, 101):
                res = square_root_test(number, iter_count)
                if res:
                    row += "   +    | "
                else:
                    row += "   -    | "
            
            File.write(f"{row}\n")

ind_2()