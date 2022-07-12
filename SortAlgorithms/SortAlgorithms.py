#bubble sorting

def swap(list1, x, y):
    list1[x], list1[y] = list1[y], list1[x]
    return

def bubbleSort(nums):
    isSorted = False
    count = 0

    while isSorted == False:
        performedSwap = False
        for i in range(len(nums)-1-count):
            #if right num is smaller, then swap
            if nums[i] > nums[i+1]:
                swap(nums, i, i+1)
                performedSwap = True
        
        if performedSwap == False:
            print(count)
            isSorted = True
        
        # print(nums)
        count += 1
        if count == len(nums)-1:
            isSorted = True

myList = [1,7,18,21,4,5,20,22,10]
bubbleSort(myList)
print(myList)

#sliding bars
def insertionSort(nums):
    for i in range(1, len(nums)):
        j=i
        while j>0 and nums[j] < nums[j-1]:
            swap(nums, j, j-1)
            j-=1
myList = [1,7,18,21,4,5,20,22,10]
insertionSort(myList)
print(myList)