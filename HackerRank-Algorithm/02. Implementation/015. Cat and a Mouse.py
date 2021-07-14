def CatAndMouse(catA, catB, mouseC):
    distanceA = abs(catA - mouseC)
    distanceB = abs(catB - mouseC)
    if(distanceA > distanceB):
        print("Cat B")
    elif(distanceA < distanceB):
        print("Cat A")
    else:
        print("Mouse C")
        
        
n = int(input())
for i in range(n):
    catA, catB, mouseC = map(int, input().split())
    CatAndMouse(catA, catB, mouseC)
