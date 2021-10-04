# the input arr is a list, the output long is a number.
# arr[i] is a positive integer.
# n is the len of the list arr.
# for example arr = [8,7,3,5,4] -> [8,7,3] [8,7,5] [8,7,4] [8,5,4] [7,5,4] -> long = 5
def morgan(arr):
    n = len(arr)
    long = 0
    repeat = []
    if n <= 2:
        long = 0
    elif n > 2:
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (arr[i] > arr[j]) and (arr[j] > arr[k]):
                        if [arr[i], arr[j], arr[k]] not in repeat:
                            repeat.append([arr[i], arr[j], arr[k]])
                            long += 1
                            print(arr[i], arr[j], arr[k])
                    elif (arr[i] > arr[j]) and (arr[j] <= arr[k]):
                        k += 1
                    elif arr[i] < arr[j]:
                        j += 1
    return long

# test cases

if __name__ == '__main__':
    array = [8, 7, 3, 5, 4, 6, 2, 8, 9, 11, 4, 7, 455, 327162, 1, 1, 8, 199, 456, 422, 190, 3671819, 177, 10]
    num = morgan(array)
    print(num) 


