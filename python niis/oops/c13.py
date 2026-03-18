class p:
    def property(self):
        print("land+money+car")

    def marry(self):
        print("sita")


class C(p):
    def marry(self):
        print("gita")


ob = C()
ob.property()
ob.marry()