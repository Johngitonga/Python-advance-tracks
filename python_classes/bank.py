"""
You have just started working at a bank, and you discover that they aren't using any computers to keep track of their
customers!

Create some Python classes that will keep track of your customers.
Each customer should have a first and second name, as well as an ID number (4 digits). They also have the option to deposit
money when they open the account (default amount to start is 0 for most customers)

All customers can get their balance for free

There should also be methods in your classes for depositing and withdrawing. See the rules for the different customers below.

Your bank has 3 types of customers:
Regular -  no minimum balance, starting balance is whatever they put in at the beginning. Charged 50 kes withdrawal fee.

Preferred - Must maintain a minimum balance of 10000 kes, not charged a withdrawl fee.

Student - No minimum balance, no withdrawal fee, but can only withdraw 500 kes at a time.

If a customer tries to withdraw more than is in his/her account, goes below the minimum balance,
 or if a student tries to withdraw more than 500kes, print out an error message.
 """

class Customer(object):
	
	def __init__(self, first_name, second_name, id_number, bal):
		self.first_name = first_name
		self.second_name = second_name
		self.id_number = id_number
		self.withdrawal_charge = 0
		self.minimun_bal = 0
		self.max_withdraw = False
		self.bal = bal

	def deposit_money(self, cash):
		self.cash =  cash
		self.bal+=cash
		

	def withdraw_money(self, amount):
		self.amount = amount
		if self.amount > self.bal:
			print "oops!, You are not allowed to have an overdraft"
		elif (self.bal - self.amount) < self.minimun_bal:
			print "You must have a min bal of ", self.minimun_bal
		elif self.max_withdraw and self.amount > self.max_withdraw:
			print "You are not allowed to withdraw more than 500 in one transaction"			
		else:
			self.bal-=amount
			return self.bal

	def check_balance(self):
		return "You balance is {} ".format(self.bal)
	
class Regular(Customer):
	def __init__(self, *args):
		super(Regular, self).__init__(*args)
		self.minimun_bal = 0
		self.withdrawal_charge = 50
		
class Preferred(Customer):
	def __init__(self, *args):
		super(Preferred, self).__init__(*args)
		self.minimun_bal=10000
		self.withdrawal_charge = 0
		
class Student(Customer):
	def __init__(self, *args):
		super(Student, self).__init__(*args)
		self.max_withdraw = 500
		self.minimun_bal = 0
		self.withdrawal_charge = 0
					

#person = Customer("John", "Gitonga", 2460, 0)
# john = Regular("regular","john",'g',1111,1000)
# john.deposit_money(5000)
# john.rules()
# print john.withdraw_money(2000)

# mary = Preferred("mary",'t',3847, 0)
# mary.deposit_money(12000)
# mary.deposit_money(12000)

# mary.withdraw_money(200)
# print mary.check_balance()

# #person.deposit_money(5000)
# #person.withdraw_money(500)
# #print person.check_balance()
learner = Student("Richard", "Branson", 2222, 0)
learner.deposit_money(2350)
learner.withdraw_money(550)
print learner.check_balance()


