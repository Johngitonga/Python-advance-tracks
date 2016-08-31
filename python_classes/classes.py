# Your Code here
class Person(object):

	def __init__(self, first_name, middle_name, surname, number):
		self.first_name = first_name
		self.middle_name = middle_name
		self.surname = surname
		self.number = number

class Student(Person):

	POSTGRADUATE = "POSTGRADUATE"
	UNDERGRADUATE = "UNDERGRADUATE"

	def __init__(self, student_type, *args):
		self.student_type = student_type
		self.classes = []
		super(Student, self).__init__(*args)
		

	def enrol(self, course):
		self.classes.append(course)


class StaffMember(Person):	
	TEMPORARY = "TEMPORARY"
	PERMANENT = "PERMANENT"

	def __init__(self, membertype, *args):
		
		self.employment_type = membertype
		super(StaffMember, self).__init__(*args)

class Lecturer (StaffMember):

	def __init__(self, membertype, *args):
		StaffMember.__init__(self, membertype, *args)
		self.courses_taught = []

	def assign_teaching(self, courses):
		self.courses_taught.append(courses)

	
#Random person 
random_person = Person("Johnson", "Mwelusi", "Mwema", 0000)
print random_person.first_name #"Johnson"
print random_person.middle_name #"Mwelusi" 
print random_person.surname #Mwema
print random_person.number #"0000"

# Student 1
jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "Thomson" "0000", "POSTGRADUATE")
print jane.first_name #"Jane"
print jane.middle_name #"Smith"
print jane.surname #Thomson
print jane.number #"0000"
print jane.student_type #"POSTGRADUATE"
jane.enrol("Introduction to data science")
jane.enrol("IOT")
print jane.classes #['Introduction to data science', 'IOT']

#Student 2
john = Student(Student.UNDERGRADUATE, "John", "Jay", "Larson", 1123)
print john.first_name #"John"
print john.middle_name #"Jay"
print john.surname #"Larson"
print john.number #"1123"
print john.student_type #"UNDERGRADUATE"
john.enrol("Introduction to python")
john.enrol("Introduction to DBs")
print john.classes #['Introduction to python', 'Introduction to DBs']


#Random staffmember
staff_member = StaffMember(StaffMember.TEMPORARY, "Bob", "A.", "Jackson", "535")
print staff_member.employment_type #TEMPORARY
print staff_member.first_name #"Bob"
print staff_member.middle_name #"A."
print staff_member.surname #"Jackson"
print staff_member.number #"535"


#Lecturer
helen = Lecturer(StaffMember.PERMANENT, "Helen", "B.", "Jess", "1234")
print helen.employment_type #PERMANENT
print helen.first_name #"Helen"
print helen.middle_name #"B."
print helen.surname #"Jess"
print helen.number #"1234"
helen.assign_teaching("Introduction to data science")
helen.assign_teaching("Introduction to DBs")
print helen.courses_taught #['Introduction to data science', 'Introduction to DBs']

#all work is done