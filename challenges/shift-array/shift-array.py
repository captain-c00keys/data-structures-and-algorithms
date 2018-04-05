def insertShiftArray (prior_array , value):


    if len(prior_array) > 0 and len(prior_array) % 2 == 0:
        middle = len(prior_array)//2
    elif len(prior_array) > 0 and len(prior_array) % 2 == 1:
        middle = len(prior_array) % 2 == 1
    else:
        middle = 0

    new_array = [0] * (len(prior_array)+1)

    for i in range(middle):
        new_array[i] = prior_array[i]
    new_array[middle] = value
    
    for i in range(middle + 1, len(new_array)):
        new_array[i] = prior_array[i - 1]
    return(new_array)

insertShiftArray([10, 20, 40, 50], 35)