a = [-8,12,15,-10,13,1,18,-2]
outputSum = 0
tempList = []
tempSum = 0
outputList = []
x = 0
for i in range(len(a)):
    if (a[i] <= 0):
        if(tempSum > outputSum):
            outputSum = tempSum
            outputList = tempList
        tempSum = 0
        tempList = []
    else:
        tempList.append(a[i])
        tempSum += a[i]
print outputSum
print outputList