class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, rollno, course):
        Person.__init__(self, name, age)
        self.rollno = rollno
        self.course = course

    def show_student(self):
        print("Roll Number:", self.rollno)
        print("Course:", self.course)


class Engineering(Student):
    def __init__(self, name, age, rollno, course, branch, college):
        Student.__init__(self, name, age, rollno, course)
        self.branch = branch
        self.college = college

    def show_engineering(self):
        print("Branch:", self.branch)
        print("College:", self.college)



obj = Engineering("tapan", 20, 101, "B.Tech", "Computer Science", " niis")

obj.show_person()
obj.show_student()
obj.show_engineering()