def Square_root_3():
    c = 2
    g = c/2
    i = 0
    while(abs(g*g - c) > 0.00000000001):
        g = (g + c/g)/2
        i += 1
        print("%d:%.13f"%(i,g))

def Square_root_4():
    c = 2
    g = c
    i = 0
    while(abs(g*g - c) > 0.00000000001):
        g = (g + c/g)/2
        i += 1
        print("%d:%.13f"%(i,g))

def Square_root_5():
    c = 2
    g = c/4
    i = 0
    while(abs(g*g - c) > 0.00000000001):
        g = (g + c/g)/2
        i += 1
        print("%d:%.13f"%(i,g))

Square_root_3()
print("")
Square_root_4()
print("")
Square_root_5()