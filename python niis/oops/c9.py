# alternate method of getter and setter 
class Student:
    def __init__(self, n, r, m):
        self.__name = n
        self.__roll = r
        self.__mark = m

    def show(self):
        print("my name =", self.__name)
        print("my rollno =", self.__roll)
        print("my mark =", self.__mark)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value


s = Student("tapan", 60, 90.5)

print("Name =", s.name) 
s.name = "rohit"          

s.show()
