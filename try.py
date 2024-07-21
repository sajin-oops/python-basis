# List = [3,4,5,-2,-1,2,8,0,-4]. Move all negative numbers to the end of the list.
def find(arr):
    arr.sort(reverse=True)
    print(arr)
array = [3,4,5,-2,-1,2,8,0,-4]
find(array)

# output - [8, 5, 4, 3, 2, 0, -1, -2, -4]