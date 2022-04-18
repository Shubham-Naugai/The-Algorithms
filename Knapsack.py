""" 0/1 Knapsack (bounded) """


max_weight = 7
weight_array = [1, 3, 4]
value_array = [10, 5, 4]
n = len(weight_array) # = len(value_array)

## Recursive approach
def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    if wt[n-1] <= w:
        return max(val[n-1]+knapsack(w-wt[n-1], wt, val, n-1), knapsack(w, wt, val, n-1))
    elif wt[n-1] > w:
        return knapsack(w, wt, val, n-1)

print(knapsack(max_weight, weight_array, value_array, n))


## Memoization
lookUp = [[-1 for x in range(max_weight + 1)] for x in range(n + 1)]

def knapsackMemo(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    if lookUp[n][w] != -1:
        return lookUp[n][w]
    if wt[n-1] <= w:
        lookUp[n][w] = max(val[n-1]+knapsackMemo(w-wt[n-1], wt, val, n-1), knapsackMemo(w, wt, val, n-1))
        return lookUp[n][w]
    elif wt[n-1] > w:
        lookUp[n][w] =  knapsackMemo(w, wt, val, n-1)
        return lookUp[n][w]

print(knapsackMemo(max_weight, weight_array, value_array, n))


## Top-Down

def knapsackTopDown(w, wt, val, n):
    lookUp = [[-1 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                lookUp[i][j] = 0
            elif wt[i-1] <= j:
                lookUp[i][j] = max(val[i-1] + lookUp[i-1][j-wt[i-1]], lookUp[i-1][j])
            else:
                lookUp[i][j] =  lookUp[i-1][j]
    return lookUp[n][w]

print(knapsackTopDown(max_weight, weight_array, value_array, n))
