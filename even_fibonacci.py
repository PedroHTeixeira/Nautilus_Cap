# GIT 17/11/2020 10:00 Part-2
i=2
l = [1,2]
s = 0
j=0
while l[-1] <4*10**6:
    l.append(l[i-2]+ l[i-1])
    i=i+1

for j in l:
    if j % 2 == 0 :
        s = s +j
print(s)