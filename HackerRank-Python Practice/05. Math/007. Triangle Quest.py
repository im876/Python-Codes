for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*((pow(10,i)-1)//(9)))
    
#how this works:
#1       1 * i
#22      11 * i
#333     111 * i
#4444    1111 * i

#so for i = 1: pow(10,1)//9 => 10^1//9 => 10//9 => 1
#for i = 2 : pow(10,2)//9 => 10^2//9 => 100//9 => 11 and so on
