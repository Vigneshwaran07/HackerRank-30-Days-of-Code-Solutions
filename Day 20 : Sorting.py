n = input()
a = list(map(int, input().split()))
count = 0
for i in range(0,len(a)):
    for j in range(i, len(a)):
        if (a[i] > a[j]):
            a[i],a[j] = a[j],a[i]
            count += 1
    if(count==0):
        break
print("Array is sorted in "+str(count)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))
