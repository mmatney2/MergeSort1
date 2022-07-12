def duplicate_count(text):
    n = text.lower()
    count = 0
    dict = {}
    for i in range(0,len(text)):
        dict[text[i]]=0
        # print(i)
    for key in dict:
        for i in range(0,len(text)):
            if(key == text[i]):
                dict[key] = dict[key] + 1
    for key in dict:
        if(dict[key] > 1):
            count = count + 1
    return count
print(duplicate_count("aabbcssa"))

def noRepeat(s):
    d={}
    for letter in s:
        d[letter] = d.get(letter,0) + 1
    for i in range(len(s)):
        if d[s[i]]==1:
            return i
    return -1
print(noRepeat("aabbcss"))

def persistence(n):
    s = 0
    t = 1
    while (n > 9):
        if t == 1:
          t = n % 10
        n -= n %10
        n /= 10
        t *= (n % 10)
        if (n <= 9) :
          n = t
          t = 1
          s += 1
    return s

# Replace With Alphabet Position
def alphabet_position(text):
    text = text.lower()
    res = ""
    index = 0
    while index < len(text):
        item = text[index]
        print(item)
        if ord(item) > ord("z") or ord(item) < ord("a"):
          index += 1
          continue
#         print item,ord(item)-ord("a")
        res += str(ord(item)-ord("a")+1) + " "
        index += 1
    return res[:-1]
print(alphabet_position(("The sunset sets at twelve o' clock.")))

def duplicate_encode(word):
    word = list(map(lambda x: x.lower(), word))
    unique = set(word)
    unique_counts = {}
    for elem in unique:
        unique_counts[elem] = word.count(elem)
      
    output = ""
    for elem in word:
        if unique_counts[elem] < 2:
            output += '('
        else:
            output += ')'
    return output

def duplicate_count(text):
    n = text.lower()
    count = 0
    d = {}
    for i in range(0,len(n)):
        d[n[i]] = 0
        print(i)
    for key in d:
        for i in range(0,len(n)):
            if(key == n[i]):
                d[key] = d[key] + 1
    for key in d:
        if(d[key] > 1):
            count = count + 1
    return count
print(duplicate_count("abede"))

def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList

def to_camel_case(text):
    list = [x for x in text]
    if len(list) != 0: 
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list

def deck(hand):
    suit = {
        "H",
        "D",
        "C",
        "S"
    }
    deck2 = []
    for i in range(len(hand)):
        if hand[i] in suit:
            if hand[i-1] == "0":
                letter = hand[i-2] + hand[i-1]
                card = letter + hand[i]
                deck2.append(card)
            else:
                letter = hand[i-1]
                card = letter + hand[i]
                deck2.append(card)
    return deck2
print(deck("5H8DKS10CJD"))


# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
# from collections import Counter
def common_strings(words):
    dict={}
    first_time=True
    #loop through the words of the list
    for word in words:
        temp={}
    # #split up all letters of the words
        for letter in word:
            if letter in temp:
                temp[letter]+=1
            else:
                temp[letter]=1
        if first_time:
            dict=temp
            first_time= False
            continue
        for letter in dict:
            if letter != temp:
                dict[letter]=0
            else:
                dict[letter]=min([dict[letter, temp[letter]]])
    output=[]
    for letter in dict:
        output+=[letter]*dict[letter]
    return output
print(common_strings(["bella","label","roller"]))
            
words =['bella','label', 'roller']
def dups(words):
    store=[]
    for word in words: #n
        if not store:
            store=list(word)
            continue
        else:
            for letter in store: #n
                if letter not in set(word):
                    store.remove(letter) #n
            if not store:
                return []
    return store

print(dups(words))

            
        
    #break down the words

    #find the common letters

print(common_strings(["cool","lock","cook"]))

#Given a list of numbers containing one duplicate value, return the duplicated value.
# Input:
nums=[1, 2, 3, 2, 4]
# Output:
# 2

#count method
def fd(nums):
    for num in nums:
        if nums.count(num)>1:
            return num

print("Z1",fd([1, 2, 2, 3, 4]))
print("Z2",fd([3, 1, 3, 4, 2]))
print("Z3",fd([3, 1, 4, 4, 8]))

#Dictionary
def find_duplicate(nums):
    from collections import Counter
    c = Counter(nums)
    for k, v in c.items():
        if v > 1:
            return k


print("A1",find_duplicate([1, 2, 2, 3, 4]))
print("A2",find_duplicate([3, 1, 3, 4, 2]))
print("A3",find_duplicate([3, 1, 4, 4, 8]))

#Math
def find_dup(nums):
    sumnums = sum(nums)
    sumset = sum(set(nums))
    return (sumnums - sumset)


print("B1",find_dup([1, 2, 2, 3, 4]))
print("B2",find_dup([3, 1, 3, 4, 2]))
print("B3",find_dup([3, 1, 4, 4, 8]))

# If the numbers are all consecutive
# Tortoise and the Hare Algorithm
# https://davidfloyd91.github.io/floyd-tortoise-hare-cycle-linked-list-python/
def find_duplicate2(nums):
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
print("C1",find_duplicate2([1, 2, 2, 3, 4]))
print("C2",find_duplicate2([3, 1, 3, 4, 2]))
print("C3",find_duplicate2([3, 1, 4, 4, 2]))

def duplicates(nums):
    dups = set()
    for num in nums:
        if num in dups:
            return num
        else:
            dups.add(num)

print(duplicates(nums))

