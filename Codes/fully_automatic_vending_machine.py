'''
Problem Statement

FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:

Coffee

Espresso Coffee
Cappuccino Coffee
Latte Coffee
Tea

Plain Tea
Assam Tea
Ginger Tea
Cardamom Tea
Masala Tea
Lemon Tea
Green Tea
Organic Darjeeling Tea
Soups 

Hot and Sour Soup
Veg Corn Soup
Tomato Soup
Spicy Tomato Soup
Beverages

Hot Chocolate Drink
Badam Drink
Badam-Pista Drink
Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):

Welcome to CCD 

Enjoy your

Example 1:

Input:
c
1
Output
Welcome to CCD!
Enjoy your Espresso Coffee!
Example 2:

Input
t
9
Output
INVALID OUTPUT!
'''

menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

'Badam-Pista Drink']]

m = input("Enter c for Coffee, t for Tea, s for Soup, b for Beverages: ")

if(m == 'c' or m == 't' or m == 's' or m == 'b'):
    if(m == 'c'):
        print("Displaying Menu for Coffee:")
        for i in menu[0]:
            print("*",i)
        submenu = int(input())
        if(submenu in range(1,4)):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[0][submenu-1]))
        else:
            print("INVALID INPUT")
    if(m == 't'):
        print("Displaying Menu for Tea:")
        for i in menu[1]:
            print("*",i)
        submenu = int(input())
        if(submenu in range(1,9)):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[1][submenu-1]))
        else:
            print("INVALID INPUT")
    if(m == 's'):
        print("Displaying Menu for Soup:")
        for i in menu[2]:
            print("*",i)
        submenu = int(input())
        if(submenu in range(1,5)):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[2][submenu-1]))
        else:
            print("INVALID INPUT")
    if(m == 'b'):
        print("Displaying Menu for Beverage:")
        for i in menu[3]:
            print("*",i)
        submenu = int(input())
        if(submenu in range(1,4)):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[3][submenu-1]))
        else:
            print("INVALID INPUT")
else:
    print("INVALID INPUT")
