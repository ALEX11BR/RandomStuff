import random
import time

size=5
arr = [1]*size

def getAvailable(arr):
    size = len(arr)
    max1 = arr[0]
    max1p = [0]
    max2 = 0
    max2p = []
    for i in range(1, size):
        if max1 == arr[i]:
            max1p.append(i)
        elif max1 < arr[i]:
            max2 = max1
            max2p = max1p
            max1 = arr[i]
            max1p = [i]
        if max2 == arr[i]:
            max2p.append(i)
        elif max2 < arr[i] and max1 > arr[i] or max2 == 0:
            max2 = arr[i]
            max2p = [i]
    print(arr, max2p, max2)
    return max2p

def oneGen(arr):
    size = len(arr)
    if random.randrange(0, 3) == 0:
        toSub = random.randrange(0, size)
        if arr[toSub] > 1:
            arr[toSub] -= 1
    available = getAvailable(arr)
    toAdd = random.choice(available)
    arr[toAdd] += 1

while True:
    oneGen(arr)
    print(arr)
    time.sleep(1)