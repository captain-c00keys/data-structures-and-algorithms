def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    mid = len(arr) // 2

    print('start: ', start, ', mid: ', mid, ', end: ', end)

    while start + 1 != end:
        if arr[mid] == x:
            print('index of: ', x, ' is ', mid)
            return mid
        elif arr[mid] > x:
            end = mid
        elif arr[mid] < x:
            start = mid
        mid = ((end - start) // 2) + start

        print('start: ', start, ', mid: ', mid, ', end: ', end)

    print(-1)
    return -1


binary_search([4,8,15,16,23,42],15)