class Account:
    min_bal:500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposit_amount(self,amount):
        print("Instance Method")
print(Account.__dict__)