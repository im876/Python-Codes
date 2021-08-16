#countPalin() function counts the number of palindrome words by extracting every word of the string and passing it to 
#checkPalin() function. An extra space is added in the original string to extract last word. 

#checkPalin() function check the word palindrome. It returns 1 if word is palindrome else returns 0. 
#It makes sure that empty strings are not counted as palindrome as the user may enter more than one spaces in 
#between or at the beginning of the string. 


def countPalin(string):
    count = 0
    for i in string:
        if(checkPalin(i)):
            count += 1
    return count

def checkPalin(i):
    if(i.lower() == i.lower()[::-1]):
        return True
    
string = input().split()
print("Number of palindrome words in string are:",countPalin(string))
