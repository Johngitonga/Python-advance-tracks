class Dog:
	def __init__(self, name):
		self.name=name

	def barking(self, barking_sound):
		return barking_sound

first_dog = Dog("Jack")
oscar = Dog("Oscar")
print first_dog.name
print first_dog.barking("woof woof")

print oscar.name
print oscar.barking("Yap yap")