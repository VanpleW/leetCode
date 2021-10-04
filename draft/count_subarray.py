'''
# split the array to 3-elements subarrays with desending order, 
# array a, split as [a[i], a[j], a[k]], where i < j < k < len(a) and a[i] > a[j] > a[k];
# a contains only positive integer
# output the number of subarrays without repeated one: number
'''

def count_subarray(input_array):
    number = 0
    result = []
    first_part = input_array
    n = len(first_part)
    if n < 3:
        return 0

    # eliminate maximum first element over and over again
    while len(first_part) > 2:
        first = max(first_part)
        first_index = first_part.index(first)
        
        second_part = first_part[first_index+1:]
        # remove the same number of second element in last part
        if first in second_part:
            second_part.remove(first)
        # eliminate maximum second element over and over again
        while len(second_part) > 1:
            second = max(second_part)
            second_index = second_part.index(second)

            # find the number of subarrays by the third elements
            third_part = second_part[second_index +1 : ]
            # remove the same number of second element in last part
            third_part = [i for i in third_part if i != second]
            # use set to eliminate the duplicates
            third_part = set(third_part)
            
            third_length = len(third_part)
            # count the number in
            number =  number + third_length
            for third in third_part:
                result.append([first, second, third])
            # remove the used second element
            second_part = [i for i in second_part if i != second]

        # remove the used first element
        first_part = [i for i in first_part if i != first]

    return number, result

# test cases
from tabulate import tabulate

if __name__ == '__main__':
    array = [8, 7, 3, 5, 4, 6, 2, 8, 9, 11, 4, 7, 455, 327162, 1, 1, 8, 199, 456, 422, 190, 3671819, 177, 10]
    num, result = count_subarray(array)
    print(tabulate(result))
    print(num)