import random
global regionmodifier
regionmodifier = 1


class Player():
    def __init__(self, name):
        self.name = name
        self.health = hp
        self.currenthp = self.health
        self.level = 1
        self.exp = 0
        self.attack = 0
        self.defense = 0
        self.damage = 0

    def damage(self):
        points = monsterattack
        self.currenthp -= points

    def exp(self):
        self.exp + expdrop
        if self.exp >= 10 + 1.1 * self.level - 1:
            self.level += 1
            self.exp -= (10 + 1,1 * (self.level - 1) -1)


class Monster():
    def __init__(self, monstertype, regionmodifier):
        self.type = monstertype
        
        if monstertype == 1:
            self.health = 2 
            self.attack = 1
            self.expdrop = random.randint(1, 10)

        elif self.type == 2:
            self.health = 4
            self.attack = 2
            self.expdrop = random.randint(10, 25)

        elif self.type == 3:
            self.health = 6
            self.attack = 3
            self.expdrop = random.randint(25, 40)
            
        self.health = round(self.health + 0.1 * player.level * regionmodifier)
        self.attack = round(self.attack + 0.1 * player.level * regionmodifier)
        
    def damage(self):
        points = playerattack
        self.health -= points

    def get_health(self):
        print(self.health)

player = Player('player', '1')
monster = Monster(1, regionmodifier)
