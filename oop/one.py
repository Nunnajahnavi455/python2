class Employee:     #here class is a template 
    loc_id='101'
e1=Employee()       #by constructing object class is used
e2=Employee()       #object
e3=Employee()       #object
print(id(e1))
print(id(e2))
print(id(e3))
print(e1.__dict__) #
print(e2.__dict__)
print(e3.__dict__)