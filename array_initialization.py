#   Single level array ----------------------

arr = [-1] * 4
arr[0] = 5
print(arr)  #    [5, 0, 0, 0]

arr = [0 for i in range(4)] 
arr[0] = 5
print(arr)  #    [5, 0, 0, 0]


#   Multi level array ----------------------

arr = [[0] * 4] * 3
arr[1][1] = 5
print(arr)  #    [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
#   Problem : All subarrays are references to the same array

arr = [[0] * 4 for i in range(3)]
arr[1][1] = 5
print(arr)  #    [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]
#   Solved : All subarrays are unique