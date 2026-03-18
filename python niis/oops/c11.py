class demo:
    def show(self, a):
        print("one argument show",a)
    def show(self ,a,b):
        print("two arguments show",a,b)
    def show(self):
        print("no arguments show") 
d=demo()
d.show()
d.show(10)
d.show(10,20)                 		