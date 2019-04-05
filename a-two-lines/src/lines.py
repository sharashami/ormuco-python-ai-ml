
def overlap(x1, x2, x3,x4):
    
    float(x1)
    float(x2)
    float(x3)
    float(x4)

    if x1 == x2 or x3 == x4:
        raise ValueError('a line cannot have the same start and end value')
    
    line1 = [x1 , x2]
    line1.sort()
    line2 = [x3 , x4]
    line2.sort()
    return ( line1[0] >= line2[0] and line1[0] <= line2[1] ) or ( line1[1] >= line2[0] and line1[1] <= line2[1] )
        
    