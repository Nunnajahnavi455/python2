class Gp:
    def m1(self):
        print("Gp-class m1 method")
        
    def m2(self):
        print("Gp-class m2 method")
        
class Parent(Gp):
    def m3(self):
        print("Gp-class m3 method")
    
class child(Parent):
    def m4(self):
        print("Gp-class m4 method")
obj=child()
obj.m1
obj.m2
obj.m3
obj.m4