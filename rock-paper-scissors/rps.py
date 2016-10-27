'''
INITIAL NOTE:
-------------
You will be provided with unittests for all the scenarios described below
	Setup
	------
	This exercise is heavily relying tests. You will need to install two test modules for you to work 
	smoothly.
	The modules are 'nose' and 'sure' as listed in requirements.txt.
		links:
			sure --> https://sure.readthedocs.io/en/latest/
			nose --> http://nose.readthedocs.io/en/latest/testing.html 

	It is good practice to use a virtualenv while developing 
		link:
			virtualenv --> http://docs.python-guide.org/en/latest/dev/virtualenvs/

	To install the two modules mentioned above just run (Make sure your are in your virtualenv) 
		 pip install -r requirements.txt
	
	Running the test file
	---------------------
	To run the testfile (make sure you are in the virtualenv that you installed nose and sure in)
	use the command	
		nosetests
	while you are in the root directory of the project i.e inside rock-paper-scissors directory.

P-SET
------
In a game of rock-paper-scissors, each player chooses to play Rock (R),
Paper (P), or Scissors (S). The rules are: Rock breaks Scissors, Scissors
cuts Paper, but Paper covers Rock. 

In a round of rock-paper-scissors, each player's name and strategy is
encoded as an array of two elements
    ['Kimani', 'Rock']  => Kimani plays Rock
    ['Kevo', 'Paper']   => Kevo plays Paper

(In this example, Kevo would win because Paper covers Rock.)

PART 1: GAME LOGIC
-------------------
Create a RockPaperScissors class with a *class* method `winner` that
takes two 2-element arrays like those above, and returns the one
representing the winner:

    RockPaperScissors.winner(['Kimani', 'Rock'], ['Kevo', 'Paper']) # => This should return ['Kevo', 'Paper']

If either player's strategy is something other than "Rock", "Paper" or "Scissors"
(case-SENSITIVE), the method should raise a
'RockPaperScissors.NoSuchStrategyError' exception
			[research about exceptions]

If both players use the same strategy, the first player is the winner.


PART 2: TOURNAMENT
-------------------
A rock-paper-scissors tournament is encoded as an array of games -
that is, each element can be considered its own tournament.
		[
      [
        [["John", "Paper"], ["Kelvin", "Scissors"]],
        [["Mick", "Rock"], ["Fred", "Scissors"]],
      ],[
        [["Anne", "Scissors"], ["Cess", "Paper"]],
        [["Renice", "Rock"], ["Patrick", "Paper"]]
      ]
   	]

Under this scenario, Kelvin would beat John (S>P) and Mick would
beat Fred (R>S), so Kelvin and Mick would play (Mick wins since
R>S); similarly, Anne would beat Cess, Patric would beat Renice.,
and Anne and Patric would play (Anne wins since S>P); and finally
Mick would beat Anne since R>S.  That is, pairwise play continues
until there is only a single winner. 

Write a class method `RockPaperScissors.tournament_winner'
that takes a tournament encoded as an 
array and returns the winner (for the above example, it should return
["Mick", "Rock"]). 

Go on further and test the tournament between 52 players

	HINT: Formulate the problem as a recursive one whose base case you
	solved in part 1.
'''

import random

class RockPaperScissors(object):
	
	play = ['Rock', 'Paper', 'Scissors']

	class NoSuchStrategyError(StandardError):
		pass

	@classmethod
	def winner(self, player_one, player_two):
		self.player_one = player_one
		self.player_two = player_two
		# self.shoot =  random.choice(RockPaperScissors.play)

		#Exception
		if self.player_one[1] not in RockPaperScissors.play or self.player_two[1] not in RockPaperScissors.play:
			raise self.NoSuchStrategyError('That is not a legal shot ')
		
		#If a tie
		elif self.player_one[1] == self.player_two[1]: #or self.player_two[1] == self.player_one[1]:
			return self.player_one
		#Paper vs scissors
		elif self.player_one[1] == 'Paper' and self.player_two[1] == 'Scissors':
			return self.player_two
		elif self.player_one[1] == 'Scissors' and self.player_two[1] == "Paper":
			return self.player_one
		#Paper vs rock
		elif self.player_one[1] == 'Paper' and self.player_two[1] == 'Rock':
			return self.player_one
		elif self.player_one[1] == 'Rock' and self.player_two[1] == "Paper":
			return self.player_two
		#Scissors vs rock
		elif self.player_one[1] == 'Scissors' and self.player_two[1] == 'Rock':
			return self.player_two
		elif self.player_one[1] == 'Rock' and self.player_two[1] == "Scissors":
			return self.player_one

	@classmethod
	def tournament_winner(self, team):

		if type(team[0][0]) == str:
			
			return RockPaperScissors.winner(team[0], team[1])

		
		team_one = team[0]
		team_two = team[1]
		return RockPaperScissors.winner(RockPaperScissors.tournament_winner(team_one), RockPaperScissors.tournament_winner(team_two))


		 		
		 


			

tournament = [
      [
        [["John", "Paper"], ["Kelvin", "Scissors"]],
        [["Mick", "Rock"], ["Fred", "Scissors"]],
      ],[
        [["Anne", "Scissors"], ["Cess", "Paper"]],
        [["Renice", "Rock"], ["Patrick", "Paper"]]
      ]
    ]


# print RockPaperScissors.winner(['Kimani', 'Rock'], ['Kevo', 'Rock'])	
# print RockPaperScissors.winner(['Kimani', 'Paper'], ['Kevo', 'Paper'])	
print RockPaperScissors.tournament_winner(tournament)
