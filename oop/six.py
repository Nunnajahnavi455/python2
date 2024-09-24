class Test:
    def __init__(self):
        print("Test class-Constructor Method")
    def m1(self):
        print("Test class-Instance Method")
    @classmethod
    def m2(cls):
        print("Test class-class Method")
    @staticmethod
    def m3():
        print("Test class-static Method")
t1=Test()
t2=Test()
t1.m1()
t1.m1()