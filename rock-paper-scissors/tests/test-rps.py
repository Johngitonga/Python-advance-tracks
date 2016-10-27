import sure
import unittest 

from rps import RockPaperScissors

class RPS_Test(unittest.TestCase):
  def setUp(self):
    self.player1 = ['Kimani', 'Rock']
    self.player2 = ['Kevo', 'Paper']
    self.player3 = ['Cess', 'Scissors']

  def test_rock_breaks_scissors(self):
		(RockPaperScissors.winner(self.player1, self.player2)).should.be.equal(self.player2)
  
  def test_paper_covers_rock(self):
    (RockPaperScissors.winner(self.player1, self.player3)).should.be.equal(self.player1)
  
  def test_scissors_cut_paper(self):
		(RockPaperScissors.winner(self.player2, self.player3)).should.be.equal(self.player3)
  
  def test_first_player_wins_if_both_use_same_strategy(self):
    (RockPaperScissors.winner(['Gitonga', 'Rock'], self.player1)).should.be.equal(['Gitonga', 'Rock'])

  def test_should_raise_NoSuchStrategyError_if_strategy_isnt_Rock_Paper_or_Scissors(self):
    self.assertRaises(RockPaperScissors.NoSuchStrategyError, 
      lambda: RockPaperScissors.winner(self.player1, ['Mary', 'Spork']))

class RPS_Tournament(unittest.TestCase):
  def test_base_case(self):
    tournament = [['Kimani', 'Rock'], ['Cess', 'Scissors']]
    (RockPaperScissors.tournament_winner(tournament)).should.be.equal(['Kimani', 'Rock'])

  def test_recursively_get_the_winner_from_8_people_tournament(self):
    
    tournament = [
      [
        [["John", "Paper"], ["Kelvin", "Scissors"]],
        [["Mick", "Rock"], ["Fred", "Scissors"]],
      ],[
        [["Anne", "Scissors"], ["Cess", "Paper"]],
        [["Renice", "Rock"], ["Patrick", "Paper"]]
      ]
    ]
    (RockPaperScissors.tournament_winner(tournament)).should.be.equal(['Mick', 'Rock'])
  
  def test_recursively_get_the_winner_from_52_people_tournament(self):
    tournament = [ 
      [
        [
          [
            [
              [['Donte Salais ', 'Paper'], ['Annamaria Canterbury ', 'Paper']],
              [['Velia Chesser ', 'Paper'], ['Yaeko Kamer ', 'Scissors']], 
            ],[
              [['Gia Rutten ', 'Rock'], ['Clarita Shy ', 'Scissors']], 
              [['Lou Teaster ', 'Rock'], ['Samira Lebeau ', 'Paper']],
            ]
          ],[ 
            [['Isaias Knudtson ', 'Rock'], ['Ethel Denson ', 'Scissors']],
            [['Trish Fowkes ', 'Rock'], ['Noble Denzer ', 'Scissors']],
          ]  
        ],[
          [
            [
              [['Zelma Spinner ', 'Scissors'], ['Tressa Winfield ', 'Paper']], 
              [['Chelsie Sholes ', 'Paper'], ['Marget Portier ', 'Scissors']], 
            ],[
              [['Charlie Kemper ', 'Rock'], ['Elmo Hartz ', 'Paper']], 
              [['Lavera Letchworth ', 'Rock'], ['Tammie Elsberry ', 'Rock']],
            ] 
          ],[
            [['Argentina Wojcik ', 'Scissors'], ['Johana Muller ', 'Scissors']], 
            [['Tory Chapell ', 'Paper'], ['Jeanetta Sarinana ', 'Paper']],
          ]
        ] 
      ],
      [
        [
          [
            [
              [['Kandy Devlin ', 'Scissors'], ['Rosalia Manigault ', 'Paper']], 
              [['Melynda Iraheta ', 'Paper'], ['Ebony Villalon ', 'Paper']], 
            ],[
              [['Katina Gaudin ', 'Paper'], ['Del Mysliwiec ', 'Rock']], 
              [['Pearly Doolittle ', 'Paper'], ['Lilliana Kreiner ', 'Paper']], 
            ]
          ],[
            [['Sanjuanita Bragg ', 'Paper'], ['Manual Yoshioka ', 'Scissors']], 
            [['Dorla Toliver ', 'Scissors'], ['Hubert Chauvin ', 'Paper']],
          ] 
        ],[
          [
            [
              [['Sherril Powell ', 'Rock'], ['Gerardo Prioleau ', 'Scissors']], 
              [['Dick Gault ', 'Scissors'], ['Carmelina Colberg ', 'Paper']], 
            ], [
              [['Jarrod Brodsky ', 'Scissors'], ['Felipe Rogerson ', 'Scissors']], 
              [['Janette Tramel ', 'Paper'], ['Blanche Gwyn ', 'Rock']],
            ]
          ],[
            [
              [['Kelvin Castiglia ', 'Scissors'], ['Danika Brenneman ', 'Paper']], 
              [['Antone Pirkle ', 'Rock'], ['Bunny Linz ', 'Paper']], 
            ],[
              [['Danielle Loso ', 'Rock'], ['Ocie Rolfe', 'Scissors']],
              [["John", "Paper"], ["Kelvin", "Scissors"]]

            ]
          ]
        ]
      ]
    ]
    (RockPaperScissors.tournament_winner(tournament)).should.be.equal(['Isaias Knudtson ', 'Rock'])

    