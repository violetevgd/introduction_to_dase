s = input()
start = 0
n = len(s)
for start in range(n - 1):
    if(list(s)[start] == list(s)[start + 1]):
        print("true")
        break

