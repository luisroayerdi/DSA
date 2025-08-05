
'''
Enumerate takes list [4,2,3] -> [(0, 4),(1, 2),(2, 3)]


prevMap = {} #val:index

for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
        return [prevMap[diff], i]
    prevMap[n] = 1
return
'''
