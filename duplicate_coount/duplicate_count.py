def duplicate_count(text):
    n = text.lower()
    count = 0
    dict = {}
    for i in range(0,len(text),1):
        dict[text[i]]=0

        print(dict)
        print(text)
        print(i)

    for key in dict:
        for i in range(0,len(text)):
            if(key == text[i]):
                dict[key] = dict[key] + 1
    for key in dict:
        if(dict[key] > 1):
            count = count + 1
    return count
print(duplicate_count("aabbcss"))