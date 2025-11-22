def triangle_area(a, h): 
    '''Принимает сторону a и высоту h, возвращает площадь треугольника со стороной a и высотой h'''
    if a < 0 or h < 0:
        return -1
    if a == 0 or h == 0:
        return -2
    return a * h / 2 

def triangle_perimeter(a, b, c): 
    '''Принимает длины a,b,c и возвращает периметр треугольника с данными сторонами'''
    if a < 0 or b < 0 or c < 0:
        return -1
    if a == 0 or b == 0 or c ==0:
        return -2
    return a + b + c
    