a = [-1,0,-1,2,2]
b = []
for i in range(len(a)):
    x = max(a)
    for j in range(len(a)):
        if (a[i] < a[j] and a[j] <= x):
            x = a[j]
    b.append(x)

for i in range(len(b)):
    if (a[i] == x):
        b[i] = " "

c = []
d = ""
for i in range(len(a)):
    d = str(a[i]) + " -> " + str(b[i])
    c.append(d)
print c