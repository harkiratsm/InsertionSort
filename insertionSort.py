def insertionSort(numList):
    for index in range(1, len(numList)):
        currentValue = numList[index]
        position = index
        while position > 0 and numList[position-1] > currentValue :
            numList[position] = numList[position-1]
            position = position - 1
        numList[position] = currentValue
numList = [99,55,4,66,28,31,36,52,38,72]
insertionSort(numList)
print(numList)