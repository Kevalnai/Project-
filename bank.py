class bank():

    def __init__(self):
        self.bank='AXIS Bank'
        self.custName=input('Enter your name : ')
        self.b = int(input('Enter Opening Balance : '))

    def withDraw(self):
        print('')
        self.w=int(input('Enter Withdrawal Amount : '))
        if(self.b<=1000):
            print('!!!!!!!INSUFFICIENT BALANCE!!!!!!!')
            print('!!!!!!!Enter an amount less than or equal to your balance!!!!!!!')
        else:
            self.b=self.b-self.w
            print('Withdrawal done of Rs.',self.w)
            print('Balance after withdrawal :',self.b)


    def Deposit(self):
        print('')
        self.d=int(input('Enter Deposit Amount : '))
        self.b=self.b+self.d
        print('Deposit made of Rs.',self.d)
        print('Balance after deposit :',self.b)

    def displayBalance(self):
        print('')
        print('Bank :',self.bank)
        print('Customer Name :',self.custName)
        print('Balance :',self.b)

obj = bank()
while True:
    print("\n")
    print("==================================")
    print("**********************************")
    print("=<< 1. For WITHDRAW.           >>=")
    print("=<< 2. For DEPOSIT.            >>=")
    print("=<< 3. For DISPLAY.            >>=")
    print("=<< Press any key to Exit/Quit >>=")
    print("**********************************")
    print("==================================")
    i = input('Enter Your Choice : ')

    if (i == '1'):
        obj.withDraw()

    elif (i == '2'):
        obj.Deposit()

    elif (i == '3'):
        obj.displayBalance()

    else:
        print('EXIT')
        break