def sort(arr):
    
    lis = input
    length = len(lis)
    for i in range(length - 1):
        for j in range(i+1, length):
            if list[i] > lis[j]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp

    return lis
    