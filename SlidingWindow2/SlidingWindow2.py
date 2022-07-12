
def countsubstrings(s):
    count = 0
    for i in range(len(s)-2):
        # print(s[i:i+3])

        if len(s[i:i+3]) == len(set(s[i:i+3])):
            print(s[i:i+3])
            count += 1
    return count


s="xyzzab"
print(countsubstrings(s))