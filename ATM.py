class ATM:
    def __init__(self):
        print(id(self))
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        print('                                  HDFC')
        user_input=input('''
        Hi how can i help you?
        1. press 1 to create a pin 
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdrow money
        5. press 5 to exit.                                                  
        ''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdrow()
        else:
            exit()
    def create_pin(self):
        User_pin=input('enter the pin')
        self.pin=User_pin

        user_balance=int(input('enter the your balance'))
        self.balance=user_balance

        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('enter the old pin')

        if old_pin == self.pin:
            new_pin=input('enter the new pin')
            self.pin=new_pin
            print('pin change successful')
        else:
            print('nahi karane ke re baba')
            self.menu()
    def check_balance(self):
        user_pin=input('enter your pin')
        if user_pin==self.pin:
            print('your balance is',self.balance)
        else:
            print('these pin is worng')
            self.menu()

    def withdrow(self):
        user_pin=input('enter the pin')
        if user_pin==self.pin:
            amount=int(input('enter the amount'))
            if amount<=self.balance:
                self.balance=self.balance-amount
            
                print('withdrow successful balance is ',self.balance)
            else:
                print('their are not sufficientamount ')
        else:
            print('that is not you')
            self.menu()

obj = ATM()


        