def cost_garden(side, length, breadth, cost):
    if(side<=0 or length<=0 or breadth<=0 or cost <=0):
        return "INVALID INPUT"
    elif(length > side or breadth > side):
        return "INVALID INPUT"
    else:
        area_plot = side * side
        area_house = length * breadth
        temp = area_plot - area_house
        result = (temp * cost)/100
    return result
    

side = int(input())
length = int(input())
breadth = int(input())
cost = int(input())
print(int(cost_garden(side, length, breadth, cost)))
