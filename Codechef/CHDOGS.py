# python 3.4

test = int(input())
 
for t in range(test):
    s, v = [int(x) for x in input().split()]
    p = (2*s) / (3*v)
    if p < pow(10, -6):
        print(pow(10, -6))
    else:
        print(p)  
