""" subset sum problem """

## Recursive approach

arr = [2, 3, 7, 8, 10]
s = 11

def subsetSum(arr, n, s):
    if n>=0 and s == 0:
        return True
    elif n==0 and s>0:
        return False
    if arr[n-1] > s:
        return subsetSum(arr, n-1, s)
    return subsetSum(arr, n-1, s) or subsetSum(arr, n-1, s-arr[n-1])

print(subsetSum(arr, 5, s))


## Memoization

arr = [2, 3, 7, 8, 10]
s = 6
n = len(arr)
lookUp = [[-1 for i in range(s+1)] for j in range(n+1)]
def subsetSum(arr, n, s):
    if n>=0 and s == 0:
        return 1
    
    elif n==0 and s>0:
        return 0
    
    if lookUp[n-1][s] != -1:
        return lookUp[n-1][s]
    
    if arr[n-1] > s:
        lookUp[n-1][s] = subsetSum(arr, n-1, s)
        return lookUp[n-1][s]
    
    lookUp[n-1][s] = subsetSum(arr, n-1, s)
    return lookUp[n-1][s] or subsetSum(arr, n-1, s-arr[n-1])

print(subsetSum(arr, n, s))


## Top-Down

arr = [2, 3, 7, 8, 10]
s = 6
n = len(arr)

lookUp = [[False for i in range(s+1)] for j in range(n+1)]
def subset(arr, n, s):
    for i in range(n+1):
        for j in range(s+1):
            if i>=0 and j == 0:
                lookUp[i][j] = True
            elif i==0 and j>0:
                lookUp[i][j] = False
            elif j < arr[i-1]:
                lookUp[i][j] = lookUp[i-1][j]
            elif j >= arr[i-1]:
                lookUp[i][j] = (lookUp[i-1][j] or lookUp[i-1][j - arr[i-1]])
    return lookUp[n][s]

print(subset(arr, n, s))
