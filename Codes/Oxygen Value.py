t1 = t2 = t3 = 0
for i in range(9):
    x = int(input())
    if(1 <= x <= 100):
        if(i%3 == 0):
            t1 += x
        elif(i%3 == 1):
            t2 += x
        elif(i%3 == 2):
            t3 += x
    else:
        print("INVALID INPUT")

A1 = round(t1/3)
A2 = round(t2/3)
A3 = round(t3/3)
print(A1,A2,A3)

if(A1>=A2 and A1>=A3):
    print("Trainee Number: 1")
if(A2>=A1 and A2>=A3):
    print("Trainee Number: 2")
if(A3>=A2 and A3>=A1):
    print("Trainee Number: 3")
    
    
#The selection of MPCS exams includes a fitness test which is conducted on the ground. There will be a batch of 3 trainees, appearing for a running test on track for 3 rounds.

#You need to record their oxygen level after every round. After trainees are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds and select the one with the highest average oxygen level as the fittest trainee. If more than one trainee attains the same highest average level, they all need to be selected. Display the fittest trainee(or trainers) and the highest average oxygen level.



#Note:
#1.The oxygen value entered should not be accepted if it is not in the range between 1 and 100.
#2.If the calculated maximum average oxygen value of the trainees is below 70 then declare the trainees as unfit with a meaningful message as “All trainees are unfit”
#3.Average oxygen values should be rounded

#Example 1:
#Input #1:
#95
#92
#95
#92
#90
#92
#90
#92
#90

#Output:
#Trainee Number: 1
#Trainee Number: 3

#Note: Input should be 9 integer values representing oxygen levels entered in order as 

#Round 1: 
#Oxygen value of trainee 1
#Oxygen value of trainee 2
#Oxygen value of trainee 3

#Round 2:
#Oxygen value of trainee 1
#Oxygen value of trainee 2 
#Oxygen value of trainee 3

#Round 3:
#Oxygen value of trainee 1
#Oxygen value of trainee 2
#Oxygen value of trainee 3



Oxygen must be in the given format as in the above example. For any wrong input, the final output should display “INVALID INPUT”
