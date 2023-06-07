from functools import *
def intersect(*ar):
    return reduce(__intersectSC,ar)
def __intersectSC(listX,listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList