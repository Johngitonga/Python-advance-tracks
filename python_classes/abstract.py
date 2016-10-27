from abc import ABCMeta, abstractmethod

class Vehicle(object):
    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0
   

    def __init__(self, make, model, year, sold):
    	self.make = make
    	self.model = model
    	self.year = year
    	# self.wheels = wheels
    	self.sold = ["sold", "Available"]

    def price(self):
	    	if self.sold == self.sold[0]:
	    		return "sold"
	    	Car.base_sale_price = 4000
	    	return ("This vehicle costs {}, it has {} wheels").format(self.base_sale_price, self.wheels)

	# @abstractmethod
    def vehicle_type(self):
       
        pass

    
class Car(Vehicle):
	base_sale_price = 500000
	wheels = 4
	def __init__(self, *args):
		super(Car, self).__init__(*args)

	def vehicle_type(self):
		return "Car"
    	

class Truck(Vehicle):
	base_sale_price = 1000000
	wheels = 8
	def __init__(self, *args):
		super(Truck, self).__init__(*args)

	def vehicle_type(self):
		return "Truck"



check = Car('Benz', 'E230', '2016', "sold")
print check.price()
