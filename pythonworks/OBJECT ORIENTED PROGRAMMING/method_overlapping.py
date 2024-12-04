class Person:

    name:str

    age:int

    def _init_(self,name,age):

        self.name=name

        self.age=age


    def display_person_info(self):

        print(self.name,self.age)

    
        
class Employee:

    eid=int

    salary=int 

    def _init_(self,eid,salary,):

        self.eid=eid

        self.salary=salary

    def display_employye_info(self):

        print(self.eid,self.salary)


class Manger(Person,Employee):

    department:str

    def _init_(self,age,name,eid,salary,department):

        Person._init_(self,age,name)

        Employee._init_(self,eid,salary)

        self.department=department

    def display_manger_info(self):

        self.display_person_info()

        self.display_employye_info()

        print(self.department)


       
manage_instance=Manger(32,"hari","eo1",54000,"hr")

manage_instance.display_manger_info()