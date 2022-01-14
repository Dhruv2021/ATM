class Atm(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin

    def checkBalance(self):
        print("Your Balance Is 5 Lakhs")
    def withdrawl(self,ammount):
        newAmmount=500000-ammount
        print("The Remaining Balance is= "+str(newAmmount))

def main():
    cardNumber=input("Enter The Card Number= ")
    pinNumber=input("Enter Your Pin= ")
    newUser=Atm(cardNumber,pinNumber)
    print("Choose Your Activity")
    print("1.Balance Enquiry,2.Withdrawl")
    responce=int(input("Enter Your Response= "))
    if responce==1:
        newUser.checkBalance()
    else:
        ammount=int(input("Enter The Ammount= "))
        newUser.withdrawl(ammount)
main()