#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = ''
    count = 0
    for i in range(x):
        try:
            num = num + str(my_list[i])
            print(f'{my_list[i]}',end='')
            count += 1
        except:
            continue
    print('')    
    return(count)
