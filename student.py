class Student:
    name ="Effence"
    age =20
    country="Kenya"
    school ="Akirachix" 
    def __init__(self,name,age,country,first_name,second_name):
        self.name = name
        self.age =age
        self.country=country
        self.first_name= first_name
        self.second_name=second_name
    def greeting(self):
        return f"Hello{self.name}from {self.country}welcome to{self.school}" 
    def fullname(self):
        return f"Hello {self.first_name} {self.second_name}"
    def year_of_birth(self):
        year=2022-self.age
        return f"Hello{self.first_name} you were born in {year}"

             