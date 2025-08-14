

a='AAAAABBBAA'
mychars=list(a)
print(mychars)



#print ('A' * 5)


#data = [('A', 5), ('B', 3), ('A', 2)]
#=''
#for char, count in data:
    #res =res + (char * count)
#print (res)

#myTuple = ("John", "Peter", "Vicky")

#x = "".join(myTuple)

#print(x)




def encodeASCII(word):
    char_count = {}

    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)



def encodeASCII_other(text):
    result = []

    prev_char = text[0]
    count = 1

    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append((prev_char, count))
            prev_char = char
            count = 1

    # Append the last group
    result.append((prev_char, count))

    return result


def decodeASCII(mylist):
    x = ""
    for char, count in mylist:
        x += char * count
    return x



#print(encodeASCII('AAAAABBBAA'))
print(encodeASCII_other('AAAAABBBAA'))
print (decodeASCII([('A', 5), ('B', 3), ('A', 2)]))