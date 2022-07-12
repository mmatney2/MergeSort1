# def persistence(n):
#     count = 0
#     while n >= 9:
#         count += 1
#         t = [int(d) for d in str(n)]
#         # print(count)
#         # print(t)
#         n = 1
#         for x in t:
#             n =n* x
#             print(x)
#             print(n)
#     return count    
# print(persistence(10))



# def persistence(n, t=0):
#     n=str(n)
#     z=1
#     if len(n)!=1:
#         for x in n:
#             z=z*int(x)
#         return persistence(z, t+1)
#     else:
#         return t
# print(persistence(39))


# def persistence(n):
#     ans=0
#     if len(str(n))==1:return ans
#     s=str(n)
#     k=1
#     for i in s:
#         k*=int(i)
#     ans+=persistence(k)+1
#     return ans
# print(persistence(39))

# def duplicate_encode(w):
#     """a new string where each character in the new string is '(' 
#     if that character appears only once in the original word, or ')' 
#     if that character appears more than once in the original word. 
#     Ignores capitalization when determining if a character is a duplicate. """
#     w = w.upper()
#     r = ""
#     for c in w:
#         if w.count(c) > 1:
#             print(r)
#             r = r+ ")"
#         else:
#             r =r+ "("
            
#     return r
# print(duplicate_encode("recede"))

# # Given a word w and some text t, find whether w is in t. For example: w="nest", t="I built a nest and tested it."

# def word_text(w,t):
#     #loop thru text 
#     #look for word 
#     #if word in text, return true or false
#     new_t=t.split(' ')
#     print(new_t)
#     if w in new_t:
#         return True
#     else:
#         return False

# word="test"
# text = "I built a nest and tested it."
# print(word_text(word,text))

def to_camal_case(text):
    """Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
    The first word within the output should be capitalized only if the original word was capitalized 
    (known as Upper Camel Case, also often referred to as Pascal case)."""
    list = [x for x in text]
    print(list)
    if len(list) != 0: 
        for i in range(len(list)):
            print(i)
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list
print(to_camal_case("the_stealth_warrior"))

