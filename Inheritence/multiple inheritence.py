class parent1:
    def m1(self):
        print("Gp-class m1 method")
class parent2:
    def m2(self):
        print("Gp-class m2 method")
class child(parent1,parent2):
    print("child-")
obj=child()