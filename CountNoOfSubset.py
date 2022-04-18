# Count the number of subset with a given difference

def countOfSubsetSum(arr, s):
    n = len(arr)
    lookUp = [[False for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if i>=0 and j == 0:
                lookUp[i][j] = 1
            elif i==0 and j>0:
                lookUp[i][j] = 0
            elif j < arr[i-1]:
                lookUp[i][j] = lookUp[i-1][j]
            elif j >= arr[i-1]:
                lookUp[i][j] = (lookUp[i-1][j] + lookUp[i-1][j - arr[i-1]])
    return lookUp[n][s]

def noOfSubset(arr, diff):
    subsetSum = (diff + sum(arr))//2
    return countOfSubsetSum(arr, subsetSum)


arr = [1,1,1,1,1]
difference = 3
print(noOfSubset(arr, difference))
