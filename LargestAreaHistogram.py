# def LAH(arr):
#     stack = [] # pair: [height, maxWidth]
#     maxAreaList = []
#     for i in range(len(arr)):
#         # by default width is 1
#         width = 1
#         a = []
#         while stack and stack[-1][0] >= arr[i]:
#             a = stack.pop()
#             maxAreaList.append(a[0]*a[1])
        
#         if a and a[0] >= arr[i]:
#             width += a[1]
            
#         if stack and stack[-1][0] < arr[i]:
#             for x in stack:
#                 x[1] += 1
        
#         stack.append([arr[i], width])
    
#     for i in range(len(stack)):
#         maxAreaList.append(stack[i][0] * stack[i][1])
#     print(max(maxAreaList))

# LAH([2, 1, 5, 6, 2, 3])

def LAH(arr):
    maxArea = 0
    stack = [] #pair: (index, heights)
    for i, h in enumerate(arr):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i-index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(arr) - i))
    return maxArea
print(LAH([2, 1, 5, 6, 2, 3]))
