x="Joshua is Awesome"
y = list(x)
a = ""
b=[]
for i in range(len(y)):
    if( y[i] != " " ):
        a= a+y[i]
    else:
        b.append(a)
        a = ""
b.append(a)
x = ""
for i in range(len(b)):
    x = b[i] + " " + x
print x

