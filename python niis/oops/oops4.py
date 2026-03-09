class student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m

    def show(self):
        print("my name=",self.name)
        print("my roll no=",self.roll)
        print("my mark=",self.mark)

s1=student("tapan",60,90.50)
s2=student("rohit",55,80.50)

s1.show()
s2.show()