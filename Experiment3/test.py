import math

ans = []
for i in range(1, 1001):
    rcd = []
    for j in range(1, i):
        if i % j == 0:
            rcd.append(j)

    if sum(rcd) == i:
        ans.append(i)

for i in ans:
    print(i)