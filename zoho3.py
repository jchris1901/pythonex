import string
a = "I am Josh"
p = [" ","'",",",":",";","(",")","[","]","#","@"]
x = list(a)
l = len(x)-1
i = 0
while( i != (len(x)-1) and i < l):
    if ((x[i] not in p) and (x[l] not in p)):
        x[i],x[l] = x[l],x[i]
        l -= 1
        i += 1
    elif ( ( x[i] in p ) and ( x[l] not in p ) ):
        i += 1
    elif ( ( x[l] in p ) and ( x[i] not in p ) ):
        l -= 1
    else:
        i += 1
        l -= 1
a = ""
for i in range(len(x)):
    a = a+x[i]
print a