# Binary number listing:
bit_lst = [1, 0, 1, 1, 0]


def binary_detector(lst):
    n = 0
    power_two = []


    for item in range(0, len(lst)):
        # print lst[item], 2 ** n
        power_two.append(2 ** n)
        # print power_two[::-1]
        n += 1

    end = len(power_two)
    
    for item in lst:

        if item == 1:
            n -= 1
            print item, power_two[n:end]
            end -= 1

        else:
            n -= 1
            print item, power_two[n:end]
            end -= 1


binary_detector(bit_lst)


# Binary sequence calculator:
def return_multiple_binaries(stop):
    total = 0
    while total != stop:
        print 'decimal:',total, '=', bin(total)
        total += 1
