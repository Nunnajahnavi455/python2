class Account:
    min_Bal=500
    def open_account(self):  #here self means instance method .and self is pointer it is used to pointing to current object.
        print('Account open  success function')
    @classmethod
    def deposit(self):
        print('Account deposited')
    @staticmethod
    def withdrawl(self):
        print('Account withdrawl')
    def get_bal(self):
        print("low bal")
#when we have to declare a class in inner side then we use [self ].
#when we have to declare a class in outer side then we use [object].
a1=Account()  #creating object
a2=Account()
a3=Account()

#what class contain variables & methods
#how to print class members? a1.open_account()=>it is object.
a1.open_account()
a1.open_account()
a1.deposit()
a1.withdrawl()
a1.get_bal()