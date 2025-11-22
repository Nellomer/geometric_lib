import math

def circle_area(r):
    '''Принимает число r - радиус окружности, возвращает площадь окружности  '''
    if r < 0: 
        return -1
    if r == 0:
        return -2
    return math.pi * r * r


def circle_perimeter(r):
    '''Принимает число r - радиус окружности, возвращает периметр окружности'''
    if r < 0: 
        return -1
    if r == 0:
        return -2
    return 2 * math.pi * r