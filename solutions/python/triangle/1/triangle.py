def equilateral(sides):
    a,b,c = sorted(sides)
    if a == b and a== c and b==c and (a != 0 and b!= 0 and c!= 0):
        return True 
    else:
        return False
def isosceles(sides):
    a,b,c = sorted(sides)
    if a+b <= c:
        return False
    return a == b or a== c or b==c
def scalene(sides):
    a,b,c = sorted(sides)
    if a == b or a== c or b==c or a+b <= c:
        return False
    else:
        return True
