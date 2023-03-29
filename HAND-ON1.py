class Person:
  def __init__(self,student,prelim,midterm,finals):
    self.__prelim = prelim
    self.__midterm = midterm
    self.__finals = finals
    self.__student = student


  def display(self):
    print("the score of the",self.__student,"in prelim is", self.__prelim)
    print("the score of the",self.__student,"in midterm is", self.__midterm)
    print("the score of the",self.__student,"in finals is", self.__finals)
    print("the average of the",self.__student,"of the semester is",(self.__prelim + self.__midterm + self.__finals)/3)

class Std1(Person):
  pass
class Std2(Person):
  pass
class Std3(Person):
  pass

std1 = Std1("Std1",75,87,67)
std1.display()
std2 = Std2("Std2",78,60,90)
std2.display()
std3 = Std3("Std3",90,87,86)
std3.display()