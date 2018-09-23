n = int(input())
d = {}
for i in range(1, n+1):
    s = input().split(' ')
    d[s[0]] = s[1]
while(1):
    a = input()
    if(a != ''):
        if a in d:
            print(a+"="+d[a])
        else:
            print("Not found")
    else:
        break
