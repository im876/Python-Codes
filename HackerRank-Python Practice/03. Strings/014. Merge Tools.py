def merge_the_tools(string, k):
    # your code goes here
    l=[]
    m=0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m+=k
    for v in l:
        #print(list(v)) :prints substring
        #print(dict.fromkeys(list(v))) :creates dictionary
        #print(dict.fromkeys(list(v).keys())) :creates keys
        #print(list(dict.fromkeys(list(v).keys()))) :makes list from those keys
        print(''.join(list(dict.fromkeys(list(v)).keys()))) #makes that list into string

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
