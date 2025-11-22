def rectangle_area(a, b): 
    '''Принимает стороны a и b, возвращает площадь прямоугольника со сторонами a и b'''
    if a < 0 or b < 0:
        return -1
    if a == 0 or b == 0:
        return -2
    return a * b 

def rectangle_perimeter(a, b):
    '''Принимает стороны a и b, возвращает периметр прямоугольника со сторонами a и b''' 
    if a < 0 or b < 0:
        return -1
    if a == 0 or b == 0:
        return -2
    return 2 * (a + b)