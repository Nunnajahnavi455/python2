class Account:
    acc_Bal=0
    def deposit_amount(self,amount):
        self.acc_Bal=self.acc_Bal+amount
a1=Account() #rahul
a2=Account()  #sonia
print(a1.__dict__)
print(a2.__dict__)

a1.deposit_amount(5000)
a2.deposit_amount(1000)

print(a1.__dict__)
print(a2.__dict__)