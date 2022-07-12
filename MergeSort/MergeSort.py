#1 - splist everything into its own group
#2 - from left to right, merge groups together
#3 - while merging, place each item in the correct position within the merged group
#4 - continue steps 3-4 until 1 group is left

def mergeSort(nums):
    #step 1 - divide into equal halves
    if len(nums)>1:
        mid = len(nums)//2
        lefthalf = nums[:mid]
        righthalf = nums[mid:]

        #recursively split left and right halves if needed
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #index pointer for the 3 lists
        i=0 #pojnter for left
        j=0 #pointer for right
        k=0 #pointer for main list

        #step 2: merge lists
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nums[k] = lefthalf[i]
                i += 1
            else:
                nums[k] = righthalf[j]
                j += 1
            k += 1
        
        #step 3: when one side finishes... place the other list into the main array
        while i < len(lefthalf):
            nums[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            nums[k] = righthalf[j]
            j += 1
            k += 1
    return
myList = [4, 20, 10, 5, 13, 10, 22]
mergeSort(myList)
print(myList)
