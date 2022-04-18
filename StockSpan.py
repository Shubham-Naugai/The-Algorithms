# Stock Span Problem
def SS(arr):
    output = []
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            output.append(-1)
        elif stack[-1][0] > arr[i]:
            output.append(stack[-1][1])
        elif stack[-1][0] <= arr[i]:
            while len(stack)>0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1][1])
        stack.append([arr[i], i])
    op = []
    for i in range(len(arr)):
        op.append(i-output[i])
    return op
print(SS([100, 80, 60, 70, 60, 75, 85]))
