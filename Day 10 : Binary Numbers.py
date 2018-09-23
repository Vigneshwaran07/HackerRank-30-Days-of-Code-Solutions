a = str(bin(int(input()))[2:])
m = 0
l = a.split('0')
for i in l:
    if(len(i) >=1 and m < len(i)):
        m = len(i)
print(m) 
