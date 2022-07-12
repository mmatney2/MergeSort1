def lengthofsubstring(s):
    longest = 0
    seen = {}
    l=0
    r=0
    for i in range(len(s)):        
        if s[r] in seen:
            l = max(seen[s[i]], l)
        longest = max(longest, i - l + 1)
        seen[s[i]] = 1 + i
    return longest



s="abcabcbb"
print(lengthofsubstring(s))