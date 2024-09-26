class InsufficientBalError(Exception):
       def __init__(self,msg):
        self.msg=msg

def withdrawl():
    amount=int(input("enter Amount to withdrawl"))
    acc_bal=5000
    if acc_bal>amount:
        print("Withdrawl and enjoy")
    else:
        raise InsufficientBalError("Low Bal")
withdrawl()
print("GOOD MORNING")