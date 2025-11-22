def square_area(a):
    '''Принимает число a , возвращает квадрат числа a'''
    if a < 0: 
        return -1
    if a == 0:
        return -2
    return a * a


def square_perimeter(a):
    '''Принимает число a, возвращает число a умноженное на 4'''
    if a < 0: 
        return -1
    if a == 0:
        return -2
    return 4 * a