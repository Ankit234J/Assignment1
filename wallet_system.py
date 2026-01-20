class Wallet:
  def __init__(self,Owner_name:str,balance:int):
    self.Owner_name =Owner_name
    self.balance= balance
    if balance <0:
      self.balance =0
    else:
      self.balance=balance

  def add_money(self,amount):
    self.balance=self.balance + amount
    print("updated balance",self.balance)

  def spend_money(self,amount):
    if self.balance >=amount:
      self.balance =self.balance -amount
      print("update balance",self.balance)
    else:
      print("Not enough money!")

  def display_info(self):
    print("Owner name:",self.Owner_name)
    print("Current Balance:",self.balance)

  def __add__(self,other):
    return Wallet("Combined Wallet", self.balance + other.balance)

  def __gt__(self,other):
    return self.balance > other.balance
  
  def __lt__(self,other):
    return self.balance < other.balance
  
  def __eq__(self,other):
    return self.balance == other.balance
  
  def weekly_allowance(self,amount):
    self.balance += amount
    return self.balance
  
  def saving_goal(self,goalamount):
    if self.balance >=goalamount:
      print('reached')
    else:
      print("not reached")

  def spendmoney_withcoupon(self,amount,coupon):
    discount = amount *(coupon/100)
    final_amount =amount -discount

    if final_amount <=self.balance:
      self.balance -=final_amount
      print("Amount spent :" ,final_amount)
      print("Reamining Balance :",self.balance)
    else:
      print("Not enough balance")

   

Wallet1 =Wallet("Ankit",280)
Wallet2= Wallet("Jaiswal",345)

Wallet1.add_money(5)
Wallet2.add_money(1)

Wallet1.spend_money(145)
Wallet2.spend_money(300)

print(Wallet1 + Wallet2)


print(Wallet1 >Wallet2)
print(Wallet1 <Wallet2)
print(Wallet1 == Wallet2)


  

