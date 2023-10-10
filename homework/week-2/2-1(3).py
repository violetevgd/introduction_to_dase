n = int(input())
b = n % 3
a = int(n / 3)
if(n < 3):
    print(n)
else:
    if(b == 0):
        print("{}个3".format(a))
    elif(b == 1):
        print("{}个,1个2".format(a-1))
    else:
        print("{}个3,1个2".format(a))