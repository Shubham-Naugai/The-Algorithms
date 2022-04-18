# Minimum subset sun difference 
# len(subset) = len(arr)/2

def minSum(nums):
    # let say sum of first subset is s1 and s2 for second
    # if s1 < s2 then s2 = totalsum - s1
    # so s2 - s1 = totalsum - 2s1 (acc to question we have to minimize this)
    """
    s = totalsum
    we know that s1 < s2 and s1 != 0 and s2 != 0
    if s1 > s/2 the s2 < s1 which is not our condition
    so we have to take only those values of s1 which are less or equal to s//2
    and those values must be sum of any subset of given arr
    where len(subset) = n = len(nums)//2
    so we get some value of s1 based on above conditions
    now totalsum - 2s1 will be min if s1 is max but less than or equal to s//2
    """
    numsLength = len(nums)
    n = numsLength / 2
    if numsLength == 2:
        return abs(nums[1] - nums[0])
    s = sum(nums)      # totalsum
    lookUp = [[False for i in range(s+1)] for j in range(numsLength+1)]
    rangearr = []

    def subset(arr, n, s):
        for i in range(n+1):
            for j in range(s+1):
                if i >= 0 and j == 0:
                    lookUp[i][j] = True
                elif i == 0 and j > 0:
                    lookUp[i][j] = False
                elif j < arr[i-1]:
                    lookUp[i][j] = lookUp[i-1][j]
                elif j >= arr[i-1]:
                    lookUp[i][j] = (
                        lookUp[i-1][j] or lookUp[i-1][j - arr[i-1]])
                # append only those values of lookup table where subset len = n
                # and subset sum j is possible(True) for that subset
                if i == n and j <= s//2 and lookUp[i][j] == True:
                    rangearr.append(j)
    subset(nums, numsLength, s)
    return s - (2 * max(rangearr))


minSum([1, 2, 3, 4])

