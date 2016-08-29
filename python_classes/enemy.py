class Enemy:
    
    def __init__(self, ranks, strength):
        self.ranks = ranks
        self.strength = strength
    def get_rank(self):
        return self.ranks
                
    def get_strength(self):
        return self.strength
        
    def get_hurt(self):
        self.strength-=5
       
        
enemy1 = Enemy('corporal', 8)
enemy2 = Enemy('Lieutenant', 16)

print enemy1.strength
