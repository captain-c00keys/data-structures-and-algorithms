from 
def fiz(numbers):
    for i in numbers:
        if i % 15 == 0:
            yield 'fizzbuzz'
        elif i % 5 == 0:
            yield 'buz'
        elif i % 3 == 0:
            yield 'fiz'
        else:
            yield str(i)


numbers = xrange(1,2**20)
print(' '.join(fiz(numbers))