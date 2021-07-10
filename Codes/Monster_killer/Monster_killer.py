health = int(input()) #health of monster
n = int(input()) #no. of attack

attack = [] #list to store attacks
no_of_attack = 0 #to store actual number of attacks

for i in range(n):
    m = int(input()) #to input number
    attack.append(m) #to add attack in the list

attack *= 2 #to multiply attacks by 2

if(health > sum(attack)):
    print("-1")
else:
    for single_attack in attack:
        if(health >= single_attack):
            health = health - single_attack
            no_of_attack += 1
            if(health == 0):
                print(no_of_attack)
    if(health > 0):
        print("-1")
