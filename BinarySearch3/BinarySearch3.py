def binarySearch(list1, target):
    list1=sorted(list1)
    left = 0 
    right = len(list1)
    while left < right:
        middle = (left + right) // 2
        potentialMatch = list1[middle]
        if target == potentialMatch:
            return f'I found my match {potentialMatch} at index {middle}' 
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return "Not Found"
x = sorted([0,1,2,3,989,852,874,55,11,235,54,66,999])

binarySearch(x, 999)

#use this to look for a page or a word in a dictionary