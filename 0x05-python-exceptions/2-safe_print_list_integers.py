#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        int_count = 0
        
        for item in my_list:
            if isinstance(item, int):
                if int_count < x:
                    print("{:d}".format(item), end=' ')
                    int_count++
                else:
                    break
            count++
        
        print()
        return (int_count)
    except:
        return (0)
