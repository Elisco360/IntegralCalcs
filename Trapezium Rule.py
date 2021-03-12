import math

from graphics import *
    
def trap():
    #eqn = input("Enter the equation in terms of x: ")
    #n = int(input("Enter the number of trapezoids: "))
    #a = eval(input("Enter the lower limit: "))
    #b = eval(input("Enter the upper limit: "))
    win = GraphWin("Trapezoidal Rule",1200,650)
    win.setCoords(0,0,10,10)

    Text(Point(5,9.5),"Welcome to Elijah's Trapezoidal Rule Calculator").draw(win)
    Text(Point(1.5,8.5),"Enter the function in terms of x: ").draw(win)
    Text(Point(1.53,8.1),"Enter the number of trapezoids: ").draw(win)
    Text(Point(1.83,7.7),"Enter the lower limit: ").draw(win)
    Text(Point(1.83,7.3),"Enter the upper limit: ").draw(win)

    input_fn = Entry(Point(2.85,8.5),8)
    input_fn.setText("x")
    input_fn.draw(win)
    input_n = Entry(Point(2.7,8.1),4)
    input_n.setText("0")
    input_n.draw(win)
    input_a = Entry(Point(2.7,7.7),4)
    input_a.setText("0.0")
    input_a.draw(win)
    input_b = Entry(Point(2.7,7.3),4)
    input_b.setText("0.0")
    input_b.draw(win)

    button = Rectangle(Point(5.7,7),Point(4.3,6.55))
    button.setFill("Orange")
    button.setOutline("Green")
    button.draw(win)
    camu = Text(Point(5,6.775),"CALCULATE")
    camu.setFill("white")
    camu.draw(win)

    win.getMouse()
    button.setFill(color_rgb(252,127,3))
    
    n = int(input_n.getText())
    a = eval(input_a.getText())
    b = eval(input_b.getText())
    
    while(a > b):
        a = eval(input("Please re-enter the lower limit: "))
        b = eval(input("Please re-enter the upper limit: "))
    
    ch_x = (b-a)/n

    comp = []

    while len(comp)!= n+1:
        print(a)
        comp.append(a)
        a = a+ch_x
        

    fn_val = []
    for x in comp:
        k = 2*math.exp(2*x)+1
        fn_val.append(round(k,4))
    r = 1
    m =[]
    for j in range(len(fn_val)-2):
        mid = 2*fn_val[r]
        m.append(mid)
        r+=1
    print("")
    print(comp)
    print("")
    print(fn_val)
    mid = sum(m)
##    print(ch_x)
##    print(comp)
##    print(fn_val)
##    print(mid)
##    print((ch_x/2),"*",fn_val[0],"+",fn_val[-1],"+",mid)
    prp = (ch_x/2)*(fn_val[0]+fn_val[-1]+mid)
    print("")
    print(round(prp,4))

    lm = 5
    ch_x = round(ch_x,4)
    fin = round(fn_val[0]+fn_val[-1]+mid,4)
    vno = fin*ch_x
    
    dis = Text(Point(lm,4.5),("T("+str(n)+") = ("+str(ch_x)+" / 2)["+str(fn_val[0])+" + 2 ("+(str(fn_val[1:-1]).replace(",","+",n-2).replace("[","").replace("]",""))+") +"+str(fn_val[-1])+"]"))
    dis.setSize(14)
    dis.draw(win)
    vn = Text(Point(5,3),("T("+str(n)+") =  "+str(vno)))
    vn.setSize(14)
    vn.draw(win)
    Line(Point(5.05,2.86),Point(5.56,2.86)).draw(win)
    xc = Text(Point(5.305,2.71),"2")
    xc.setSize(14)
    xc.draw(win)

    camu.setText("EXIT")

    Rectangle(Point(5.02,1.18),Point(5.75,1.6)).draw(win)
    pp = Text(Point(5,1.39),("T("+str(n)+") =  "+str(round(prp,4))))
    pp.setSize(18)
    pp.draw(win)

    
    win.getMouse()
    win.close()

    
trap()
