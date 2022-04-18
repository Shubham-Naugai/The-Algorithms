# Rod Cutting Problem

max_weight = 4
weight_array = [1,2,3,4]
value_array = [5,6,8,8]
n = len(weight_array) # = len(value_array)

## Top-Down
def UnboundedKnapsack(w, wt, val, n):
    lookUp = [[-1 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                lookUp[i][j] = 0
            elif wt[i-1] <= j:
                lookUp[i][j] = max(val[i-1] + lookUp[i][j-wt[i-1]], lookUp[i-1][j])
            else:
                lookUp[i][j] =  lookUp[i-1][j]
    return lookUp[n][w]

print(UnboundedKnapsack(max_weight, weight_array, value_array, n))


