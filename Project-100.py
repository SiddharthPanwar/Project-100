class Atm(object):
    def __init__(self, cardNo, pin):
        self.cardNo = cardNo
        self.pin = pin

    def cashWithdrawal(self):
        cashNeeded = input("Enter How much cash do you want?")
        print("Cash Given")

    
Card = Atm(123456789,1110)
Card.cashWithdrawal()