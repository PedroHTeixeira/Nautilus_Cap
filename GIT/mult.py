# GIT 17/11/2020 10:00 Part-1 HW
i=0
j=0
l = []
s = 0
while i < 1000:
    l.append(i)
    i = i+1

for j in l:
    if j%3 == 0 or j%5==0:
        s += j

print(s)
