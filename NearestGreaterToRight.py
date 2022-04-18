# Nearest Greater to right
def NGR(arr):
    output = []
    stack = []
    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            output.append(-1)
        elif stack[-1] > arr[i]:
            output.append(stack[-1])
        elif stack[-1] <= arr[i]:
            while len(stack)>0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])
    return output[::-1]
print(NGR([1, 2, 1, 3]))