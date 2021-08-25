"""
A group of developers generated their internal secret technique of data encode and decode. Technique for encoding is such that from the original message of text,
each characters ASCII value is found and that value is added with constant value of '5' and converted back to character for that new ASCII value and provided as changed message

Reverse is performed for decoding i.e each character ASCII values is found and subtracted with constant value of '5' and converted back to character for that new ASCII value.

NOTE:
Special character apart from ',' and '.' and numbers would print "INVALID INPUT"
If no text is entered also "INVALID INPUT" would be printed

EXAMPLES:
Input:
Hello, Sir
sjji yt yfqp
Output:
Mjqqt, Xnw
need to talk

Input:
Hello, 8Sir
Ljkuxqp
Output:
INVALID INPUT
"""



import re

def encoding(input1):
    temp = list(input1)
    result = []
    new_char = 0
    new_string = " "
    for i in range(len(input1)):
        if(',' in temp[i] or ' ' in temp[i]):
            result.append(temp[i])
        else:
            new_char = ord(temp[i]) + 5
            result.append(chr(new_char)) 
    new_string = ''.join(result)
    return new_string

def decoding(input2):
    temp = list(input2)
    result = []
    new_char = 0
    new_string = " "
    for i in range(len(input2)):
        if(',' in temp[i] or ' ' in temp[i]):
            result.append(temp[i])
        else:
            new_char = ord(temp[i]) - 5
            result.append(chr(new_char)) 
    new_string = ''.join(result)
    return new_string

input1 = input()
input2 = input()

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')


#CHECK CONDITIONS FOR INPUT1 and INPUT2
if(len(input1)==0 or len(input2)==0):
    print("INVALID INPUT")
elif(regex.search(input1) == None and regex.search(input2) == None):
    print(encoding(input1))
    print(decoding(input2))
else:
    print("INVALID INPUT")
