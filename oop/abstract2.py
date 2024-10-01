from abc import ABC
class Bank(ABC):
    def cal_tax(self):
        pass
    b=Bank()
    print(id(b))