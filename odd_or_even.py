ip = int(input())
if(ip>=1 and ip<=100000):
    if(ip%2 == 0):
        print("even")
    else:
        print("odd")
else:
    print("invalid")
