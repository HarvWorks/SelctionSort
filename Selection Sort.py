import random
import time
array = []
for i in range(0,10000):
    array.append(int(round(random.random()*1000000)))
print array

startTime1 = time.time()
def selectionSortSlow(arr):
    sortNum = 0
    length = len(arr)
    while sortNum < length:
        Min = sortNum
        for i in range(sortNum,length):
            if (arr[Min] > arr[i]):
                Min = i
        temp = arr[Min]
        arr[Min] = arr[sortNum]
        arr[sortNum] = temp
        sortNum += 1
    print arr

selectionSortSlow(array)
endTime1 = time.time()



startTime2 = time.time()
def selectionSortFast(arr):
    sortNum = 0
    length = len(arr)/2+1
    while sortNum < length:
        Min = sortNum
        Max = sortNum
        for i in range(sortNum,length):
            if (arr[Min] > arr[i]):
                Min = i
            if (arr[Max] < arr[i]):
                Max = i
        temp = arr[Min]
        arr[Min] = arr[sortNum]
        arr[sortNum] = temp
        temp = arr[Max]
        arr[Max] = arr[length-sortNum-1]
        arr[length-sortNum-1] = temp
        sortNum += 1
    print arr

selectionSortFast(array)
endTime2 = time.time()




print ("Slow Selection Sort took: %s seconds. Fast Selction Sort took: %s seconds." %(endTime1 - startTime1, endTime2 - startTime2))
