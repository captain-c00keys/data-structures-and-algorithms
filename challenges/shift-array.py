def insert_shift(arr, x):
    new_arr = [0] * (len(arr) + 1)
    print('start :: ', new_arr)
    mid_pt = len(new_arr) // 2
    i = 0
    for i in range(0, len(new_arr)):
        print('i :: ', i)
        if i < mid_pt:
            new_arr[i] = arr[i]
        if i == mid_pt:
            new_arr[i] = x
        if i > mid_pt:
            new_arr[i] = arr[i - 1]
        i += 1

    print('end :: ', new_arr)