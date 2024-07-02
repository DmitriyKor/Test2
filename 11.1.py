def prime_generator(end):
    if end<2:
        return
    num=2
    d = {}
    while num<=end:
        yield num
        ind = num*num
        while ind<=end:
            d[ind] = -1  #flag -1, ind cannot be a simple number
            ind = ind + num
        num +=1
        while d.get(num, None) == -1:
            num +=1

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
