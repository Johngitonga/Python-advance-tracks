"""
THE REMOTE GARAGE DOOR
You just got a new garage door installed. Your son (obviously when you are not home) is having a lot of fun playing with the remote 
clicker, opening and closing the door, scaring your pet dog Siba and annoying the neighbors.
The clicker is a one-button remote that works like this:
If the door is OPEN or CLOSED, clicking the button will cause the door to move, until it completes the cycle of opening or closing.
    Door: Closed -> Button clicked -> Door: Opening -> Cycle complete -> Door: Open.
If the door is currently opening or closing, clicking the button will make the door stop where it is. When clicked again, 
the door will go the opposite direction, until complete or the button is clicked again.
We will assume the initial state of the door is CLOSED.

pseudo
if door == open: button clicked
"""
 
class GarageDoor(object):
	status = "closed"
	# def __init__(self):
	# 	# self.status = "closed"
	# 	pass

	@classmethod
	def cycle_complete(self):
		if GarageDoor.status == 'opening':
			GarageDoor.status = 'open'

			print GarageDoor.status
		elif GarageDoor.status == 'closing':
			GarageDoor.status = 'closed'
			print GarageDoor.status
			
	@classmethod
	def button_clicked(self):
		if GarageDoor.status == 'closed':
			GarageDoor.status = 'opening'
			print 'The door is {}'.format(GarageDoor.status)

		elif GarageDoor.status == 'opening':
			GarageDoor.status = 'stoped while opening'
			print 'The door {} '.format(GarageDoor.status) 

		elif GarageDoor.status == 'open':
			GarageDoor.status = 'closing'
			print 'The door is {}'.format(GarageDoor.status)

		elif GarageDoor.status == 'closing':
			GarageDoor.status = 'stoped while closing'
			print GarageDoor.status

		elif GarageDoor.status == 'stoped while closing':
			GarageDoor.status = 'opening' 
			print GarageDoor.status

		elif GarageDoor.status == 'stoped while opening':
			GarageDoor.status = 'closing'
			print GarageDoor.status

		
			
	def transition(self, func):
		func()

    	

# status = "closed"
# door = GarageDoor()
# status = GarageDoor.button_clicked(status)
# status = GarageDoor.cycle_complete(status)
# status = GarageDoor.button_clicked(status)
# status = GarageDoor.cycle_complete(status)
# # print status

'''
Given some test cases the output should resemble the output in the picture
'''

# Test case 1 Output(https://github.com/tunapanda/Python-advance-tracks/blob/master/images/output1.png)
# Your son just open and closed the door on day1 and left it closed

door_on_day1 = GarageDoor()
door_on_day1.transition(GarageDoor.button_clicked) # Note button_clicked is a function
door_on_day1.transition(GarageDoor.cycle_complete) #  Note cycle_complete is a function
door_on_day1.transition(GarageDoor.button_clicked)
door_on_day1.transition(GarageDoor.cycle_complete)
print "The final state of the door is {}".format(door_on_day1.status) # # Note state is not a function 

print "********************************"
doorTest = GarageDoor()
doorTest.transition(GarageDoor.button_clicked) # Note button_clicked is a function
doorTest.transition(GarageDoor.cycle_complete) #  Note cycle_complete is a function
doorTest.transition(GarageDoor.button_clicked)
doorTest.transition(GarageDoor.button_clicked)
doorTest.transition(GarageDoor.button_clicked)
doorTest.transition(GarageDoor.cycle_complete)
doorTest.transition(GarageDoor.button_clicked)
doorTest.transition(GarageDoor.cycle_complete)
doorTest.transition(GarageDoor.button_clicked)
print "The final state of the door is {}".format(doorTest.status)
print "********************************"

# Test case 2 Output(https://github.com/tunapanda/Python-advance-tracks/blob/master/images/output2.png)
# The next day, he just had to do more experiments with the door. He clicked clicked a lot.
# The list below is the sequence of actions to the garage door
action_sequence = [GarageDoor.button_clicked, GarageDoor.cycle_complete, GarageDoor.button_clicked,
                   GarageDoor.button_clicked, GarageDoor.button_clicked, GarageDoor.button_clicked,
                   GarageDoor.button_clicked, GarageDoor.cycle_complete]

door_on_day2 = GarageDoor()
   
for action in action_sequence:
    door_on_day2.transition(action)

print "The final state of the door is {} ".format(door_on_day2.status)
