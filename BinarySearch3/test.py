def runningSum(nums):
    #for the index of the list starting at index 1 and going to the end
    for i in range(1, len(nums)):
        #add to the value at index "i" the value of index "i - 1"
        nums[i] += nums[i - 1]
    return nums

    

n = [1,2,3,4]
print(runningSum(n))
#index 2 = index 1+index 2
#index 3 = index 2+index 3
#get the index of 2 and 1 to equal the sum of value 2+1
#  nums[1] + nums[2] OR nums[i] + nums[i - 1]


def pivotIndex(nums):
    #nums = [1,7,3,6,5,6]
    #add all numbers
    s = sum(nums)
    #call left sum 0
    leftsum = 0
    #get value and index
    for i, x in enumerate(nums):
        if leftsum == (s - leftsum - x):
            return i
            
        leftsum += x
    return -1
a=[1,7,3,6,5,6]
print(pivotIndex(a))

def alternate(nums):
    sums = sum(nums)
    leftsum = 0
    for i in range(0, len(nums)):
        # print(i)
        # print(nums[i])
        if leftsum == (sums - leftsum - nums[i]):
            return i
        leftsum += 1
        # print(leftsum)
    return -1

b=[1,7,3,6,5,6]
print(alternate(b))
        