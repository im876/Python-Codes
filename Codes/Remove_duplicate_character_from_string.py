#input a string , and remove duplicate characters in string from left to right
#input = ishan modi
#output = ishan mod

def remove_dupli_char(n):
    s = ""
    for i in n:
        if(i in s):
            pass
        else:
            s += i
    return s

n = input()
print(remove_dupli_char(n))
