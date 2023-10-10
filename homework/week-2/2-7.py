def cube_root_():
    c = 10
    g = c/3
    i = 0
    while(abs(g*g*g - c) > 0.00000000001):
        g = (g * 2 + c/(g*g))/3
        i += 1
        print("%d:%.13f"%(i,g))
cube_root_()