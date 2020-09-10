#----------------------assignment1-------------------------------

print("----------------------assignment1-------------------------------")
class BankAccount:
  def __init__(self, name, balance):
    self.ownerName = name
    self.balance = balance

  def deposite(self,newbalance):
      self.balance=self.balance+newbalance
      print("Hello my name is ",self.ownerName)
      print("my balance is ",self.balance)


  def withdraw(self,newbalance):
      if(self.balance<newbalance):
          print("cant withdraw");
          return
      else:
          self.balance = self.balance - newbalance

      print("Hello my name is ", self.ownerName)
      print("my balance after withdraw " , self.balance)

p1 = BankAccount("ram",50)
p1.deposite(100)
p1.withdraw(50)

p2=  BankAccount("sham",50)
p2.deposite(100)
p2.withdraw(200)


#--------------------------------------------assignment2-------------------------------
import math

class cone:
  def __init__(self, r, h):
    self.radious = r
    self.height = h

  def volume(self):
      print("volume is: ",(math.pi*self.radious*self.radious*(self.height/3)))

  def surfacearea(self):
      print("surface area ",math.pi*self.radious*(self.radious+ math.sqrt(self.radious+self.height)))

p1 = cone(4,8)
p1.volume()
p1.surfacearea()

