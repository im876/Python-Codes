def count(temp):
    d = {}
    for i in temp:
        if i in d:
            d[i] += 1
        else :
            d[i] = 1
    s = ""
    for i in d:
        s += i+str(d[i])
    return s

string = input()
temp = string.replace(" ","")
print(count(temp))
