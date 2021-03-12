import math

def simp():
    n = int(input("Enter the number of segments: "))
    a = eval(input("Enter the lower limit: "))
    b = eval(input("Enter the upper limit: "))
    while(a > b):
        a = eval(input("Please re-enter the lower limit: "))
        b = eval(input("Please re-enter the upper limit: "))
    
    ch_x = (b-a)/n

    comp = []

    while a != (b+ch_x):
        comp.append(a)
        a = a+ch_x

    fn_val = []
    for x in comp:
        k = 2*math.exp(2*x)+1
        fn_val.append(k)

    r,r2 = 1,2
    m,m2 =[],[]
    for j in range(int(len(fn_val)/2)):
        mid = 4*fn_val[r]
        m.append(mid)
        r+=2
        
    a = int(len(fn_val)/2)
            
    for q in range(a-1):
        mid2 = math.sqrt((x**3)-1)
        m2.append(mid2)
        r2+=2
    print("")    
    print(comp)
    print("")
    print(fn_val)
##    print("")
##    print(m)
##    print("")
##    print(m2)
    mid = sum(m)
    mid2 = sum(m2)

    
    prp = (ch_x/3)*(fn_val[0]+fn_val[-1]+mid+mid2)
    print("")
    print(round(prp,4))
simp()
