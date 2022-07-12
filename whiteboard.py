import math

# #Given a string after every y add an ! and after every s add a period and make every w and g capital
# #Make a Function that takes a string as input and returns the adjusted string.
# s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
# #output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!
# def make_string(s):
#     s1 = ""
#     for letter in s:
#         #after every y I need an !
#         if letter.lower() == "y":
#             s1 += "y!"
#         #after every s I need a .
#         elif letter.lower() == "s":
#             s1 += "s."
#         #Every g needs to be capitalized
#         elif letter.lower() == "g":
#             s1 += "G"
#         #every w needs to be capitalized
#         elif letter.lower() == "w":
#             s1 += "W"
#         else:
#             s1 += letter
#     return s1
# print(make_string(s))

# # I have a list of of all the students in class
# students=["Andrew","Apollo","Cole","David","Dereck","Felix","Jessica","John", "Robert", "Saed", "Tony", "William" ]
# # David and Andrew need to meet me after class
# # Felix and Jessica need to do more Codewars
# # Robert and William and John need to finish their homework
# # and everybody else is good to go.
# # Write a function that takes a students name as an argument and returns what that student needs to do.  
# # Make sure to make the name argument case-insensitive
# # If the person in not in the class return "Get Out of My Class"
# #ex) what_to_do("David") returns: "Meet With Me After Class"
# #ex) what_to_do("Joe") returns: "Get Out Of My Class"
# #ex) what_to_do("Saed") returns: "You are Good to Go!"
# #ex) what_to_do("felix") returns: "Do More Code Wars"
# #ex) what_to_do("john") returns: "Finish your Homework"


# students = ["Andrew","Apollo","Cole","David","Dereck","Felix","Jessica","John", "Robert", "Saed", "Tony", "William" ]
# def classmates(name):

#     my_students = {
#         'andrew': 'meet me after class',
#         'david': 'meet me after class',
#         'felix':'need to do more codewars',
#         'jessica':'need to do more codewars',
#         'rober': 'finish their homework', 
#         'william': 'finish their homework',
#         'john': 'finish their homework',
#         'apollo': "You are Good to Go!",
#         'cole': "You are Good to Go!",
#         'dereck': "You are Good to Go!",
#         'sead': "You are Good to Go!",
#         'tony': 'good to go',
#         }


    
#     return my_students.get(name.title(), "You are Good to Go!")

# print(classmates('apollo'))

# def nested_sum(list):
#     first = 0
#     for num in list:
#         if isinstance(num, int):
#             first += num
#         else:
#             first += nested_sum(num)
#     return first
# list = [1, 2 [1], [1, [1], [1 [1]]]]
# print(nested_sum(list))

# def palindrom(s):
#     empty_s = ''
#     left = 0
#     right = -1
#     while left < right:
#         if s[left]==s[right]:
#             empty_s = s[left]+ s[right]
#             left += 1
#             right += -1
#     return empty_s



# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.
# # ex.1
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# # ex. 2
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]




# def arr(nums, target):
#     for a in nums:
#         if target - a in nums:
#             return [nums.index(a),nums.index(target-a)]
# print(arr([2,7,11,15],22))
# # --
# # Given an integer n, return true if it is a power of three. Otherwise, return false.

# # An integer n is a power of three, if there exists an integer x such that n == 3^x.

# # ex.1
# # Input: n = 27
# # Output: true

# # ex.2
# # Input: n = 0
# # Output: false

# # ex.3
# # Input: n = 9
# # Output: true

# # ex.4
# # Input: n = 45
# # Output: false
# def three_x(n):
#     while n > 3 and n % 3 == 0:
#         n = n/3
#     if n == 3:
#         return True
#     else:
#         return False

# def powerThree(n):
#     if n == 0:
#         return False
#     elif n == 1:
#         return True
#     else:
#         if n % 3 ==0:
#             x = n/3
#             return powerThree(x)
#         return False
    
# print(powerThree(27))
# print(powerThree(81))
# print(powerThree(45))
# print(powerThree(3))

# def nested_sum(list):
#     first = 0
#     for num in list:
#         if isinstance(num, int):
#             first += num
#         else:
#             first += nested_sum(num)
#     return first
# list = [1, 2 [1], [1, [1], [1 [1]]]]
# print(nested_sum(list))

# def palindrom(s):
#     empty_s = ''
#     left = 0
#     right = -1
#     while left < right:
#         if s[left]==s[right]:
#             empty_s = s[left]+ s[right]
#             left += 1
#             right += -1
#     return empty_s



# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.
# # ex.1
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# # ex. 2
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]




# def arr(nums, target):
#     for a in nums:
#         if target - a in nums:
#             return [nums.index(a),nums.index(target-a)]
# print(arr([2,7,11,15],22))

# # Given a string s containing just the 
# # characters '(', ')', '{', '}', '[' and ']', 
# # determine if the input string is valid.

# # An input string is valid if:

# # Open brackets must be closed by the same type of brackets.
# # Open brackets must be closed in the correct order.

# # ex.1
# # Input: s = "()"
# # Output: true

# # ex.2
# # Input: s = "()[]{}"
# # Output: true

# # ex.3
# # Input: s = "(]"
# # Output: false

# # ex.4
# # Input: s = "([)]"
# # Output: false

# # ex.5
# # Input: s = "{[]}"
# # Output: true

# def valid_string(s):
#     stack = []
#     end={')':'(', '}':'{', ']':'['}
#     for character in s:
#         if character in {'(', '{', '['}:
#             stack.append(character)
#         else:
#             if len(stack) ==0:
#                 return False
#             poppin=stack.pop()
#             if end[character] != poppin:
#                 return False
                
#     return len(stack) == 0
        
# valid_string('(((({}{}{}{}{}))))')

# # Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# # A palindrome is a word that is the same front-to-back

# # ex.1
# # Input: s = "A man, a plan, a canal: Panama"
# # Output: true
# # Explanation: "amanaplanacanalpanama" is a palindrome.

# # ex.2
# # Input: s = "race a car"
# # Output: false
# # Explanation: "raceacar" is not a palindrome.
# def palidrome(s):
#     s = ''.join([char for char in s.lower() if char.isalnum()])
#     return s==s[::-1]

# palidrome('race car')

# def palindrome(s):
#     s = s.lower()
#     left = 0
#     right = len(s)-1
#     while left < right:
#         while not s[left].isalnum():
#             left +=1
#         while  not s[right].isalnum():
#             right += -1
#         if s[left] != s[right]:
#             return False
#         elif s[left] == s[right]:
#             left += 1
#             right += -1
#     return True

# # Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# # Example
# # "abcde" -> 0 # no characters repeats more than once
# # "aabbcde" -> 2 # 'a' and 'b'
# # "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# # "indivisibility" -> 1 # 'i' occurs six times
# # "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# # "aA11" -> 2 # 'a' and '1'
# # "ABBA" -> 2 # 'A' and 'B' each occur twice

# def count(string):
#     letters = {}
#     for letter in string.lower():
#         if letter not in letters:
#             letters [letter] = 1
#         else:
#             letters [letter] += 1

#     count = 0
#     for num in letters.values():
#         if num > 1:
#             count += 1
#     return count

# print(count("aabbcde"))
# print(count("indivisibility"))
# print(count("aA11"))

# # Least Larger
# # Given an array of numbers and an index, return the index of the least number
# # larger than the element at the given index, or -1 if there is no such index.
# # Example:
# # Input: ([4, 1, 3, 5, 6], 0 ) 
# # Output: 3
# # Input: ([4, 1, 3, 5, 6], 4)
# # Output: -1

# def least_larger(numbers, index):
#     #return index of number next largest than number at given index
#     a_list = []
#     for number in numbers:
#         if number > numbers[index]:
#             a_list.append(number)
#     if not a_list:
#         return -1
#     else:
#         return numbers.index(min(a_list))
# numbers = [4, 1, 3, 5, 6]
# print(least_larger(numbers,4))
# print(least_larger(numbers,0))

# def leastLarger(lst,num):
#     d={}
#     for i in range(len(lst)):
#         if lst[i]>lst[num]:
#             d[lst[i]] = i   #key = num,  value = index
#     return d[min( d.keys() )] if len(d.keys()) else -1

# def even_or_odd(number):
    
#     if number % 2 == 0:
#         return "Even"
    
#     else:
#         return "Odd"
# print(even_or_odd(11))

# def opposite(number):
#   # your solution here
#     if number < 0:
#         return abs(number)
#     elif number > 0:
#         return number * (-1)
#     else:
#         return "it's a string"

# def number_to_string(num):
#     # Return a string of the number here!
#     return str(num)

# print(number_to_string(1))
        
# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     elif boolean == False:
#         return "No"

# def solution(string):
# #     return string[::-1]

# def positive_sum(arr):
#     new_list = []
#     for num in arr:
#         if num > 0:
#             new_list.append(num)
            
#         elif num < 0:
#             num == 0
#         elif num == 0:
#             new_list.append(num)
#         else:
#             return 0
#     return sum(new_list)

# arr = [1, -4, 8, -5, 0]

# print(positive_sum(arr))

# def find_smallest_int(arr):
#     new_list = []
#     for num in arr:
#         if num 
#             new_list.append(num)

# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

# ex.1
# calc(40,20)
# Output: 0 (The dad is twice as old as the son now!)

# ex.2
# calc(40,10)
# Output: 20 (The dad will be twice as old as his son in 20 years)

# ex.2 calc(50,30)
# # Output: 10 (The dad was twice as old as his son 10 years ago)
# def twice_old(fath_age, son_age):
#     count = 0
#     while son_age > fath_age / 2:
#         son_age -=1
#         fath_age -=1
#         count += 1
#     while son_age < fath_age / 2:
#         son_age += 1
#         fath_age +=1 
#         count += 1

# def no_space(x):
#     #your code here
#     spaceless=[]
#     if x == "":
#         return spaceless.append(x, sep="")
# print(no_space("d g h j"))

# def find_smallest_int(arr):
#     arr.sort()
#     return arr[0]
# a= [2,1,3]
# print(find_smallest_int(a))

# def count_sheeps(sheep):
#     array1 =[True,  True,  True,  False,
#     True,  True,  True,  True ,
#     True,  False, True,  False,
#     True,  False, False, True ,
#     True,  True,  True,  True ,
#     False, False, True,  True]
#     a = 0
#     for i in sheep:
#         if i == True:
#             a+=1
#         return a

# print(count_sheeps())

# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)

# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# function topk(nums, k){
#     let dict = {};
#     for (const num of nums){
#         let len = nums.filter(x => x == num).length
#         dict[num] = len
#     }
#     let ans = []
#     let values=[]
#     for (const [key, value] of Object.entries(dict)){
#         values.push(value)
#     }
#     values.sort()
#     for (let i=0; i<k; i++){
#         for (const [key, value] of Object.entries(dict)){
#             if (dict[key] == values[values.length-1]) {
#                 ans.push(key)
#                 values.pop()
#                 break
#             }
#         }
#     }
#         return ans
# }

# console.log(topk([1,1,1,2,2,3],2))

# def abbrev_name(name):
#     name.split(' ')
#     name.
#         # new_name=n.pop(0)
#         # return f"{new_name}."
# print(abbrev_name("atalie bristle"))
        
# def get_count(word):
#     if word.includes()
#     str1=word.count("a" or "e" or "i" or "o" or "u")
#     return str1
#     #     print(letter, end=' ')
#     # for l in letter:
#     #     if l == "a" or "e" or "i" or "o" or "u":
#     #         i = l.count(letter)
#     #         print(i)
# print(get_count("aaee"))

# 1 loop through a string of letters 
# #3 count the vowels
# def get_count(sentence):
#     new_list = []
#     new_list1=[]
#     for element in sentence:
#         print(element, end=' ')
#         if element == 'a'or 'e'or 'i'or 'o'or'u':
#             new_list.append(element)
#         else:
#             new_list1.append(element)
#     return new_list.count(element)
# print(get_count("aksjdhif eeeejfkdi"))


# def get_count(c):
#     newstr = c
#     vowels = ('a','e','i','o','u')
#     for x in c.lower():
#         if x not in vowels:
#             newstr = newstr.replace(x,"")
#         print(newstr, end=' ')
#     return len(newstr)
# print(get_count('asdfig oiepurio iuha'))
# #have a string
# #have a list of vowels
# #compare the two lists
# #if vowels not in 
# def get_count(txt):
#     goal = 0
#     list_one = []
#     for char in txt:
#         if char == 'a' or 'e' or 'i' or 'o' or 'u':
#             list_one.append(char)
#         goal +=1
#     return goal
# print(get_count("la;ksjd ieuy mmmaaa"))

# def incrementer(nums):
#     #parse through the list to length(add 1-len(list+1)
#     #add each length to the indexed number of the list
#     #example = [4+1, 5+2, 4+3, 3+4, 6+5, 6+6]
#     #map(function, iterable, ...)
#     return nums * 2
#     bonuses = [100,200,300]
#     x=map(lambda nums: nums+1, bonuses)

# def incrementer(nums):
#     new_list=[]
#     new_list2 =[]
#     for num in nums:   #nums=[5,3,6]
#         num =num + nums.index(num) + 1
#         new_list.append(num)
#     for new_num in new_list:
#         if new_num >= 10:
#             new_list2.append(new_num)
#         new_num=new_num-10
                
#     return new_list2



# def incrementer(nums):
#     new_list =[]
#     for num in list(nums): #nums=[5,3,6,]
#         num1 =num+ (nums.index(num) +1)
#         if num1 >=10 :
#             num1=str(num1)
#             num1=int(num1[len(num1)-1])
#         new_list.append(num1)
#     return new_list
# a=[1,2,3,6,5,13]
# print(incrementer(a))

# def inc(nums):
#     new_list=[]
#     for num in nums:
#         new_num=(num) + nums.index(num+1)
#         if new_num >=10 :
#             new_num=str(new_num)
#             new_num=int(new_num[len(new_num)-1])
#         new_list.append(new_num)
#     return new_list
# a=[0,0,0,0]
# print(inc(a))

# def disemvowel(string_):
#     newstr=string_
#     vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
#     for words in newstr:
#         if words in vowels:
#             newstr=newstr.replace(words,'')
#     # new_word = word.join(', ')
#     return newstr
# print(disemvowel("This website is for losers LOL!"))

# def square_digits(num):
#     num = str(num)
#     result=[nums for nums in num]
#     new_list=[]
#     for r in result:
#         r=int(r)
#         new_list.append(r)
#     new_list = [r**2 for r in new_list]
#     strings=[str(new_lis) for new_lis in new_list]
#     a=''.join(strings)
#     new=int(a)
#     return new

# # squares = map(square_digits, new_list)  
# # print(new_result)
# print(square_digits(564789))

# def high_and_low(numbers):
#     new = numbers.replace(' ', '000')
#     nums = [num for num in new] #turns num string into [9,8,7,0]
#     print(nums)
    # new_list=[]
    # for r in nums:
    #     r=int(r)
    #     if r != 0:
    #         new_list.append(r)
    #         # print(new_list)
    # new_list=[int(r) for r in new_list]
    # x= sorted(new_list)
    # strings=[str(new_lis) for new_lis in new_list]  
    # x= sorted(strings)
    # return f'{x[-1]} {x[0]}'
# print(high_and_low("11 3 9 4 5"))
# def high_and_low(numbers):
#     new = numbers.split(' ')
#     nums = [int(num) for num in new]
#     print(nums)
#     # new_list=[]
#     # for r in nums:
#     #     r=int(r)
#     #     new_list.append(r)
#     # new=map(int, nums)
#     # print(new)
#     # new=[int(r) for r in new]
#     x= sorted(nums)
#     return f'{x[-1]} {x[0]}'
# print(high_and_low("-111 303 -999 40 500"))

# def get_middle(s):
#     letters=[x for x in s]
#     l = len(letters)
#     middle = l//2
#     middle2=middle-1
#     y =letters[middle]
#     z=letters[middle2]
#     if l%2==0:

#         return f'{z}{y}'
#     else:
#         return y
# print(get_middle('teting'))
# def dominos(string):
#     start = 0
#     for end in range(1,len(string)):
#         if string[end] == 'R':
#             if string[start] == "R":
#                 pass
#         if string[start] == "L":


# def is_square(n):    
#     if n % math.sqrt(n)==0:
#         return True
#     if type(n) <= 0:
#         return False
#     else:
#         return False
# print(is_square(-100))

# # #25/5
# def descending_order(num):
#     num1 = list(str(num))
#     num1.sort(reverse=True)
#     str1=""
#     for e in num1:
#         str1+=e
#     str1=int(str1)
#     return str1
#     # new =", ".join([(num)for num in num1])
# print(descending_order(65489))

# def inc(nums):
#     new_list=[]
#     for num in nums:
#         new_num=(num) + nums.index(num+1)
#         if new_num >=10 :
#             new_num=str(new_num)
#             new_num=int(new_num[len(new_num)-1])
#         new_list.append(new_num)
#     return new_list

# def incrementer(nums):
#     new_list=[]
#     item = 0
#     index = 0
#     for index, item in enumerate([nums], start=1):
        
#         return list(enumerate(nums))
        


# print(incrementer([1,2,3]))

# def incrementer(nums):
#     count=1
#     new_list=[]
#     for num in nums:
#         var=num+count
#         if var>=10:
#             var=int(repr(var)[-1])
#         new_list.append(var)
#         count +=1

#     return new_list

    
# print(incrementer([1,2,9]))

    
#     # Return double of n 
# def addition(n): 
#     return n + n 
  
# # We double all numbers using map() 
# numbers = (1, 2, 3, 4) 
# result = map(addition, numbers) 
# print(list(result))

# def solution(number):
#     #get a range up to 23. 
#     #when a number is passed in, 
#         #return all the numbers below that number
#     new_list=[]
#     total=0
#     for num in range(0,number):
#         if num % 5==0 or num % 3 == 0: 
#             total = total + num
#             new_list.append(num) 
#     return sum(new_list)
# print(solution(20))

# def find_it(seq):
#     for i in range(seq):
#         count=0
#         for j in i:
#             if j==i:
#             count+=1
#             if count %2==0:
                
#         if count %2 !=0:
#             return count
# print(find_it([1,1,2,3,4]))
#     #return the intger that appears and odd 
#     #number of times 
#     #how to count each individual element that is in a list

# def nines(num):
#     num = str(num)
#     result=[nums for nums in num]
#     goal=0
#     new_list=[]
#     for i in result:
#         for j in i:
#             if '9' in j:
#                 new_list.append(j)
#                 goal+=1 
#     return goal

# # print(nines(899))

# # How many nines?
# # def nines(num):
    
# #     goal=0
# #     for i in range(0,num+1):
# #         for j in set(str(i)):
# #             if j == '9':
# #                 goal+=1 
# #                 break
# #     return goal
# # print(nines(10))

# def nines(nums):
#     count=0
    
#     for n in range(nums):
#         if '9' in str(n):
#             count+=1
#     return count

# print(nines(3950)) 

# def likes(names):
    
#     if len(names)==0:
#         return "no one likes this"
#     if len(names)==1:
#         return f'{names[0]} likes this'
#     elif len(names)==2:
#         return f'{names[0]} and {names[1]} like this'
#     elif len(names)==3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     else: 
#         return f'{names[0]}, {names[1]} and {(len(names)-2)} others like this'

      
# print(likes([]))

# def isLeapYear(year):
#     if year % 400==0:
#         return True
#     elif year %4==0:
#         return True
#     elif year % 100 ==0:
#         return False
#     elif year == 1100:
#         return False
#     else:
#         return False
# print(isLeapYear(1984))

# def nth_even(n):
#     list1=[]
#     for i in range(n):
#         if i % 2 == 0:
#             list1.append(i)
#             p=list1.index(i)
#     return p
# print(nth_even(100))

# def find_average(nums):
#     total=0
#     if nums==[]:
#         return 0  
#     for n in nums:
#         total +=n
#         x=total/len(nums)
#     return x
      
# print(find_average([1,2,3,4,5]))

# def between(a,b):
#     new_list=[]
#     for i in range(a,b+1):
#         new_list.append(i)
        
#     return new_list
# print(between(1,5))

# def add_length(str_):
#     return list(map(lambda x: " ".join([x, str(len(x))]), str_.split(" ")))
#     # for i in x:
#     #     new_list.append(f'{i}{i.index(x)}')
        


#     # return f'{x[0]} {x.index(x[0])}, {x[1]} {x.index(x[0])}'
# print(add_length("jfh hfj"))

# # def nines(num):
# #     count=0
# #     for n in range(num):
# #         if '9' in str(n):
# #             count+=1
# #     return count
# # print(nines(3950))

# def filter_list(l):
#     new=[]
#     for i in l:
#         if isinstance(i, int):
#             new.append(i)
#     return new
# print(filter_list([5,4,'a','b']))

# def is_square(n): 
#     if n<0:
#         return False
#     else:
#         for i in range(int(n/2)+1):
#             if i*i==n:
#                 return True
#             else:
#                 return False

# print(is_square(4))

# def to_jaden_case(string):
#     new=string.split(" ")
#     print(new)
#     new_list=[]
#     for word in new:
#         new_list.append(word.capitalize())
#     return " ".join(new_list)
# print(to_jaden_case("How can mirrors be real if our eyes aren\'t real"))

#find the odd int codewars
# from collections import Counter
# def find_it(seq):
#     counter = Counter(seq)
#     for num in counter:
#         if counter[num]%2!=0:
#             return num

# Sum of Digits / Digital Root
# WRONG:
# def digital_root(n):
#     while n >= 10:
#         n = sum(int(i) for i in str(n))
#     return n
# print(digital_root(926))

    # for n in nums:
    #     total +=n
    #     x=total/len(nums)
    # return x
# def digital_root2(num):
#     soma=0
#     while num//10 !=0:
#         soma += num
#     return soma
# print(digital_root2(76))


# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# #Stop gninnipS My sdroW!
# def spin_words(sentence):
#     new_list1=sentence.split()
#     new_list=[]
#     for i in new_list1:
#         if len(i)>4:
#             new_list.append(i[::-1])
#         else:
#             new_list.append(i)
#     return ' '.join(new_list)

# def array_diff(a, b):
#     for i in b:
#       if i in a:
#         for j in range(a.count(i)):
#           a.remove(i)
#     return a
# print(array_diff([1,2,3,4],[1,4]))

# def countBits(n):
#     bits = 0

#     while n > 0:
#         if n and 1:
#             bits += 1

#         n /= 2

#     return bits
# print(countBits(1234))

# from collections import Counter
# 
# def duplicate_count(text):
#     n = text.lower()
#     count = 0
#     d = {}
#     for i in range(0,len(n)):
#         d[n[i]] = 0
#         print(i)
#     for key in d:
#         for i in range(0,len(n)):
#             if(key == n[i]):
#                 d[key] = d[key] + 1
#     for key in d:
#         if(d[key] > 1):
#             count = count + 1
#     return count
# print(duplicate_count("abede"))

# def find_it(text):
#     counter = Counter(text)
#     print(counter)
#     for num in counter:
#         print(num)
#         if counter[num]%2!=0:
#             return num
            
# print(find_it("abede"))

# def find_outlier(integers):
#     even=[]
#     odd=[]
#     many=[]
#     for n in integers:
#         if n%2==0:
#             even.append(n)
#         else:
#             odd.append(n)
#     if len(odd) >len(even):
#         return even[0]
#     elif len(odd)<len(even):
#         return odd[0]
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# from collections import Counter
# def duplicate_encode(word):
#     word = list(map(lambda x: x.lower(), word))
#     unique = set(word)
#     unique_counts = {}
#     for elem in unique:
#         unique_counts[elem] = word.count(elem)
      
#     output = ""
#     for elem in word:
#         if unique_counts[elem] < 2:
#             output += '('
#         else:
#             output += ')'
#     return output

# Replace With Alphabet Position
# def alphabet_position(text):
#     text = text.lower()
#     res = ""
#     index = 0
#     while index < len(text):
#         item = text[index]
#         print(item)
#         if ord(item) > ord("z") or ord(item) < ord("a"):
#           index += 1
#           continue
# #         print item,ord(item)-ord("a")
#         res += str(ord(item)-ord("a")+1) + " "
#         index += 1
#     return res[:-1]
# print(alphabet_position(("The sunset sets at twelve o' clock.")))

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