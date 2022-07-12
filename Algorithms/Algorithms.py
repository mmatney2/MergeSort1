#swap
def swap(list1, x,y):
    list1[x], list1[y] = list1[y], list1[x]
    return

myList = [4, 20, 10, 5, 13]
print(f'before swap: {myList}')

output = swap(myList, 1, -1)

print(f'after swap: {myList}')
print('output: ', output)


#out of place
#swap
def swap(list1, x,y):
    copy = list1[:]
    copy[x], copy[y] = copy[y], copy[x]
    return copy

myList = [4, 20, 10, 5, 13]
print(f'before swap: {myList}')

output = swap(myList, 1, -1)

print(f'after swap: {myList}')
print('output: ', output)


def twoPointer(list1):
    left = 0
    right = len(list1)-1
    while left < right:
        list1[left], list1[right] = list1[right], list1[left]
        left += 1
        right -= 1
    return
myList = [1,2,3,4,5,6,22,23,25,44]
twoPointer(myList)
print(myList)