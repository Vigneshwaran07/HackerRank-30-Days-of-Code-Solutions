d1,m1,y1 = map(int, input().split())
d2,m2,y2 = map(int, input().split())
if (y1,m1,d1) <= (y2,m2,d2):
    print(0)
elif (y1,m1) == (y2,m2):  
    print(15*(d1-d2))
elif (y1==y2):
    print(500*(m1-m2))
else:
    print(10000)
