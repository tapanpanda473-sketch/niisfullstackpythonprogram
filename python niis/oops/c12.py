class demo:
    def show(self, a=None,b=None):
        if a!=None and b!=None:
        print("two argument show",a,b)
    def show(self ,a,):
        print("one arguments show",a,)
    def show(self):
        print("no arguments show") 
d=demo()
d.show()
d.show(10)
d.show(10,20)                 		