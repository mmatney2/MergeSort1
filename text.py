# num=[1,2,3,4,5]
# num.remove(2)
# print(num)


# dict={'1':'2', "3":"4"}
# given a word w and some text t, 
# find out whether w is in t
w = "nest"
t = "built a nest"

# def findWord(w,t):
#     t_list = t.split(" ")
#     print(t_list)
#     return w in t_list

# print(findWord(w,t))
def findSliding(w,t):
    l = 0
    r = 1
    while r < len(t):
        if t[r] == " " or r == len(t)-1:
            if w == t[l:r]:
                print(w)
                return True
            l = r + 1
            r = l + 1
        else:
            r += 1
    return False


print(findSliding(w,t))