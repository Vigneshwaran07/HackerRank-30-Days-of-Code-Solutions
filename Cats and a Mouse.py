n = int(input())
for i in range(n):
    a,b,c = (map(int, input().split()))
    if(abs(c-a) > abs(c-b)):
        print("Cat B")
    if(abs(c-a) < abs(c-b)):
        print("Cat A")
    if(abs(c-a) == abs(c-b)):
        print("Mouse C") 
