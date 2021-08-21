#take user inputs
Number = int(input('Enter the Number :'))
Digit = (int(input('Enter the digit :')))
#initialize Strings
String1 = str()
String2 = str()
#typecast int to str
String1 = str(Number)
String2 = str(Digit)
#count and print the occurrence
#Count function will return int value 
#so change it's type to string and concatenate it
print('Digit count is :',str(String1.count(String2)))
