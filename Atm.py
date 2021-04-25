import random
bal = random.randint(10000,90000)
balreal = bal
debt = random.randint(900,1000) 
debtreal = debt

class Atm(object):
    
    def __init__(self,card,pin,):
        self.card = card
        self.pin = pin 
    def getattributes(self):
         print(self.card, self.pin)

    def check_balance(self):

        print("Your balance is", balreal)
        endgame = input("Would you like to end the game now?")
        if(endgame == "yes"):
            return print("Ok...thanks for playing!")
        else:
            print("_____________________________")
            main()
    def withdraw(self, amount):
       new= balreal- amount
       print("You have withdrawn, ", str(amount), " and you now have $", new )
       endgame = input("Would you like to end the game now?")
       if(endgame == "yes"):
            return print("Ok...thanks for playing!")
       else:
           print("_____________________________")
           main()
    def paydebt(self, amount):
        pay = balreal - amount
        print("You have paid off ", str(amount), " of your debt, and now have ", pay, "left." )
        endgame = input("Would you like to end the game now?")
        if(endgame == "yes"):
            return print("Ok...thanks for playing!")
        else:
            print("_____________________________")
            main()
def main():
        Card_number = input("Please insert your card number here.")
        pin_number = input("Please insert your pin here.")
        print("Your current balance is", balreal, "and your current debt is, ", debtreal, ".")
        new = Atm(Card_number ,pin_number)
        activity = input("If you would like to withdraw, press w. If you want to check your balance, press k. If you want to pay off your debt, press d. ")
        if(activity == "w"):
            amount = int(input("Please enter the amount of money that you would like to withdraw."))
            new.withdraw(amount)
            main()
        elif(activity == "k"):
            new.check_balance()
        elif(activity == "d"):
            amount = int(input(" Please enter how much debt you would like to pay off."))
            new.paydebt(amount)
        else:
            print("Not a valid activity.")
main()

