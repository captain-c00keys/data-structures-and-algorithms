def multi_bracket_validation(stringInput):
    if type(stringInput) is not str:
        raise ValueError('Input a string!!')

    curly_counter = 0
    square_counter = 0
    parenthese_counter = 0

    for letter in stringInput:
        if letter is '(':
            parenthese_counter += 1
        elif letter is ')':
            parenthese_counter -= 1
        elif letter is '[':
            square_counter += 1
        elif letter is ']':
            square_counter -= 1
        elif letter is '{':
            curly_counter += 1
        elif letter is '}':
            curly_counter -= 1

    final_counter = parenthese_counter + curly_counter + square_counter

    if final_counter == 0:
        return True
    else:
        return False