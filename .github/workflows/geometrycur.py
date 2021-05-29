def rect(): 
    w = int(input('ㄱㄹ:')) 
    h = int(input('ㅅㄹ')) 
    return w * h

def tri(): 
    w = int(input('밑:')) 
    h = input(input('윗 :')) 
    return w * h / 2

def cir(): 
    
    h = int(input('ㅂ:')) 
    s = 2 * h * 3.14 
    a = h * h * 3.14 
    return s,a

while True: 
    n = int(input('1~4:')) 
    if n == 1: 
        print(rect()) 
    elif n == 2: 
        print(tri()) 
    elif n == 3: 
        print(cir()) 
    else: break 
        continue