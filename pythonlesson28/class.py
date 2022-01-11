#class Human:
#  def __init__(self,name,surname,place_of_birth,year_of_birth):
#    self.name = name
#    self.surname = surname
#    self.place_of_birth = place_of_birth
#    self.year_of_birth = year_of_birth
#  def info(self):
#    print(f"Name:{self.name},Surname:{self.surname}")
#  def year(self,years):
#    return years-self.year_of_birth
#p1 = Human("Vlad","Shatrov","UA",2004)
#p2 = Human()
#p1.info()
#b = p1.year(2022)
#print(b)
#p2.info()
#c = p2.year(2022)
#print(c)



class Human:
    def __init__(self,name,age):
      self.name = name
      self.age = age
      print("Person created")
    def info(self):
      print(f"Name:{self.name},Age:{self.age}")
    def hello(self):
      print(f"{self.name}says hello")   
class Student(Human):
    def __init__(self,name,age,course,mark):
      super().__init__(name,age)
#     Human.__init__(self,name,age)
      self.course = course
      self.mark = mark
    def studycm(self):
      print(f"Course:{self.course},Mark:{self.mark}") 
    def study(self):
      print(f"Name Student:{self.name}-studing")
    def hello(self):
      print(f"Student created")
class Teacher(Human):
    def teach(self):
      print(f"Name Teacher:{self.name}-teaches,Age:{self.age}")
s1 = Student("Vlad",17,2,200)
s1.info()
s1.study()
s1.studycm()
t1 = Teacher("Den",24)
t1.info()
t1.teach()

