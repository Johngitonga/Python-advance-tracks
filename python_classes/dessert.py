dessert_items = ["ice cream cake", "apple"]
class Dessert:
	def __init__(self, name_of_dessert, amount_of_calories):
		self.name_of_dessert = name_of_dessert
		self.amount_of_calories = amount_of_calories


	def is_healthy(self):
		if self.dessert_type()=="fruit" and self.amount_of_calories <= 400:
			return True
		return False

	def is_delicious(self):
		if self.is_healthy()==True:
			return "is delicious and is_healthy"
		return "is delicious but not healthy"		
	def dessert_type(self):
		if self.name_of_dessert == dessert_items[1]:
			return "fruit"
		return "cake"

chosen = Dessert("apple", 600)

print chosen.dessert_type()
print chosen.is_healthy()
print chosen.is_delicious()
