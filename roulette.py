import random
import turtle 


def roulette():
    money = input("How much money do you want to put up?")
    while money:
        if money.isdigit() == False or money == "0":
            print("Invalid amount. Try again")
            money = input("How much money do you want to put up?")
        else:
            money = int(money)
            break
    action = input("What would you like to do? Check money, bet, or stop playing?")
    while action:
        if action == "bet":
            money = bet(money)
            rouletteWheel()

            if money == 0:
                addMore = input("It appears you ran out of money. Would you like to add more? (Y/N)")
                if addMore == "Y":
                    money = input("How much money do you want to put up?")
                    money = int(money)
                else:
                    action = input("What would you like to do? Check money, bet, or stop playing?")

        elif action == "stop":
            print("Enjoy your earnings! Or losses...")
            break
        elif action == "money":
            print("Your current amount of money is: ",money)
            action = input("What would you like to do? Check money, bet, or stop playing?")

        else:
            print("Please enter a valid statement.")
            action = input("What would you like to do? Check money, bet, or stop playing?")

    

def bet(money):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    red = [nums[1], nums[3], nums[5], nums[7], nums[9], nums[12], nums[14], nums[16], nums[18], nums[19], nums[21], nums[23], nums[25], nums[27], nums[30], nums[32], nums[34], nums[36]]
    black = [nums[2], nums[4], nums[6], nums[8], nums[10], nums[11], nums[13], nums[15], nums[17], nums[20], nums[22], nums[24], nums[26], nums[28], nums[29], nums[31], nums[33], nums[35]]
    even = nums[2:37:2]
    odd = nums[1:37:2]
    first12 = nums[1:13]
    second12 = nums[12:25]
    third12 = nums[24:37]
    low = nums[1:19]
    high = nums[19:37]
    firstcolumn = [nums[1], nums[4], nums[7], nums[10], nums[13], nums[16], nums[19], nums[22], nums[25], nums[28], nums[31], nums[34]]
    secondcolumn = [nums[2], nums[5], nums[8], nums[11], nums[14], nums[17], nums[20], nums[23], nums[26], nums[29], nums[32], nums[35]]
    thirdcolumn = [nums[3], nums[6], nums[9], nums[12], nums[15], nums[18], nums[21], nums[24], nums[27], nums[30], nums[33], nums[36]]
    result = random.choice(nums)
    choice = input("What would you like to bet on? Included Bets: red, black, even, odd, low, high, first12, second12, third12, firstcolumn, secondcolumn, thirdcolumn, and straightup.")
    while choice:
        if choice == "red":
            print("Roulette Wheel Selected: ",result)
            if result in red:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money 
        if choice == "black":
            print("Roulette Wheel Selected: ",result)
            if result in black:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money 
        if choice == "even":
            print("Roulette Wheel Selected: ",result)
            if result in even:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "odd":
            print("Roulette Wheel Selected: ",result)
            if result in odd:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "low":
            print("Roulette Wheel Selected: ",result)
            if result in low:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "high":
            print("Roulette Wheel Selected: ",result)
            if result in high:
                money += money
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "firstcolumn":
            print("Roulette Wheel Selected: ",result)
            if result in firstcolumn:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "secondcolumn":
            print("Roulette Wheel Selected: ",result)
            if result in secondcolumn:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "thirdcolumn":
            print("Roulette Wheel Selected: ",result)
            if result in thirdcolumn:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "first12":
            print("Roulette Wheel Selected: ",result)
            if result in first12:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "second12":
            print("Roulette Wheel Selected: ",result)
            if result in second12:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "third12":
            print("Roulette Wheel Selected: ",result)
            if result in third12:
                money += money*2
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if choice == "straightup":
            bet = int(input("Which number do you bet on?"))
            print("Roulette Wheel Selected: ",result)
            if result == bet:
                money += money*36
                print("You won! You now have: ",money)
                return money
            else:
                money -= money
                print("You lost. You now have: ",money)
                return money
        if result == 0:
            print("Unlucky 0. Your money was cut in half.")
            money = money/2
            print("You now have: ",money)
            return money
        if choice == "stop":
            print("Game stopped.")
            return money

        else:
            print("Invalid Input. Try again.")
            choice = input("What would you like to bet on? Included Bets: red, black, even, odd, low, high, first12, second12, third12, firstcolumn, secondcolumn, thirdcolumn, and straightup")

             
            
def rouletteWheel():
    wn = turtle.Screen()
    wn.bgcolor("red")
    wheel = turtle.Turtle()
    wheel.hideturtle()
    wheel.speed(0)
    wheel.pensize(10)
    wheel.penup()
    wheel.goto(0,-200)
    wheel.pendown()
    wheel.pencolor("black")
    wheel.circle(200)
    
    wheel.penup()
    wheel.goto(0,-150)
    wheel.pendown()
    wheel.color("black")
    wheel.circle(150)
    wheel.pensize(15)
    for _ in range(36):
        wheel.penup()
        wheel.goto(0,0)
        wheel.left(10)
        wheel.pendown()
        wheel.forward(200)
        wheel.penup
    wheel.begin_fill()
    wheel.penup()
    wheel.goto(0,-80)
    wheel.pendown()
    wheel.color("white")
    wheel.circle(80)
    wheel.end_fill()




    

    
    

            

roulette()









        










    

    



    




