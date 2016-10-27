# Create a patient class and a doctor class. Have a doctor that can handle 
# multiple patients and setup a scheduling program where a doctor can only 
# handle 16 patients during an 8 hr work day

class Doctor (object):
	
	hours = 8
	call = "patient"
	patients = 0

	def __init__(self, name):
		self.name = "name"

	def schedule(self):
		if Doctor.hours >= 0.5:
			Doctor.call
			# print Doctor.call
			Doctor.patients+=1
			Doctor.hours-=.5
			print "{} served and {} hours left".format(Doctor.patients, Doctor.hours)
		else:
			Doctor.call = "Patient threshold of {} met".format(Doctor.patients)
			print Doctor.call
			return "First shift over. unattended patients will have to wait for second shift"

class Patient (Doctor):

	def __init__(self, *args):
		super(Patient, self).__init__(*args)

	# def shift(self):
		
		



doc = Doctor("Darius")

doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
doc.schedule()
print doc.schedule()
