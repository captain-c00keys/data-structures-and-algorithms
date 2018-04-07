

from shift-array from *


def test_shift_array_if_len_odd():
    
    prior_array = [0, 0, 0]
    value = 1
    prior_array = shift_array.insert_shift_array(prior_array, value)
    assert prior_array[2] == 1


def test_shift_array_if_len_even():
   
    prior_array = [0, 0, 0, 0]
    value = 1
    prior_array = shift_array.insert_shift_array(prior_array, value)
    assert prior_array[2] == 1


def test_shift_array_if_is_empty():
   
    prior_array = []
    value = 1
    prior_array = shift_array.insert_shift_array(prior_array, value)
    assert prior_array[0] == 1