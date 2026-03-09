class simple:
      def __init__(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t

    def calculate(self):
        si=(self.p*self.r*self.t)/100
        print("Principal =",self.p)
        print("Rate =",self.r)
        print("Time =",self.t)
        print("Simple Interest =",si)

i1=interest(1000,5,2)
i2=interest(2000,6,3)

i1.calculate()
i2.calculate()