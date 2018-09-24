import re
l = []
for i in range(int(input())):
    firstName, emailID = [str(s) for s in input().split()]
    if re.search('@gmail\.com$', emailID):
           l.append(firstName)
print(*sorted(l), sep='\n')
