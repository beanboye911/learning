class Car:
    x=0
    y=0
    vx=0
    vy=0
    name=''
    def printStatus(self):
        print('name %s x %f y %f speed x %f speed y %f' %(self.name, self.x, self.y, self.vx, self.vy))
    def speedUpx(self):
        self.vx=self.vx+1
    def speedUpy(self):
        self.vy = self.vy+1
    def drive(self, drivingTime):
        self.x=self.x+self.vx*drivingTime
        self.y=self.y+self.vy*drivingTime

car1=Car()
car1.name='fuk'
car1.printStatus()
car1.speedUpx()
car1.speedUpy()
car1.drive(10)
car1.printStatus()
car2=Car()
car2.name='shet'
car2.vx=2
car2.vy=3
car2.drive(10)
car2.printStatus()