i=0
j=0
l = []
sum = 0
while i < 1000:
    l.append(i)
    i = i+1

for j in l:
    if j%3 == 0 or j%5==0:
        sum += j

print(sum)
