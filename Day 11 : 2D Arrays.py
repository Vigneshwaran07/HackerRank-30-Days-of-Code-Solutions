a = []
for i in range(0,6):
    a.append([int(j) for j in input().split()])
tot = 0
m = 0
for i in range(0, 4):
    for j in range (0, 4):
        tot = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        if ((tot>m) or (i==0 and j==0)):
            m = tot
print(m)
