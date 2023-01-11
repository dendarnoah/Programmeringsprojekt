import random
import time
global regionmodifier
regionmodifier = 1
level = 1
exp = 0
hp = 5 + 2*level
attack = 2 + 1*level


class Player():
    def __init__(self, name):
        self.name = name
        self.health = hp
        self.currenthp = self.health
        self.level = level
        self.exp = exp
        self.attack = attack
        self.defense = 0
        self.damage = 0


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
            
        self.health = round(self.health + 0.1 * level * regionmodifier)
        self.attack = round(self.attack + 0.1 * level * regionmodifier)
        
    def damage(self):
        playerattack
        self.health -= playerattack
        print("Monstret har efter din attack", monster.health, "hp")

    def get_health(self):
        print(self.health)


class Chest():
    def __init__(self, chesttype, regionmodifier):
        self.type = chesttype

        if chesttype == träkista:
            item = random.randint(1, 100)
            if item == 1:
                item = 6
            elif item == 2:
                item = 5
            elif item >= 3 and item <= 17:
                item = 4
            elif item >= 18 and item <= 32:
                item = 3
            elif item >= 33 and item <= 64:
                item = 2
            elif item >= 65 and item <= 100:
                item = 1
            self.item = item
            self.expdrop = 2

        elif chesttype == guldkista:
            item = random.randint(1, 100)
            if item == 1:
                item = 1
            elif item == 2:
                item = 2
            elif item >= 3 and item <= 17:
                item = 3
            elif item >= 18 and item <= 32:
                item = 4
            elif item >= 33 and item <= 64:
                item = 5
            elif item >= 65 and item <= 100:
                item = 6
            self.item = item
            self.expdrop = 5


class item():
    def __init__(self, itemtype, strengthmod, defensemod):
        self.type = itemtype

player = Player('aaa')
#monster = Monster(1, regionmodifier)


sentence = "Du är en vilsen äventyrare som kommit långt hemifrån. \nDu vandrar planlöst genom skogar och ängar i vad som känns som år. \nDu kommer tillslut fram till ett samhälle.\nDu upptäcker ganska omgående att allt inte är som det ska. \nDetta samhälle är helt tomt och det ända som återfinns av en civilisation är lik. \nI skogen intill ser du rörelse, du går fram för att undersöka.\nSå fort du når fram ser du att du kan välja mellan tre stigar, vilken väljer du?"
for char in sentence:
    # Print the character and pause for a short time
    print(char, end='', flush=True)
    time.sleep(0.02)


rumsnummer = 0
dörrtyp = "stig"

while rumsnummer <=5:
    print("Välj",dörrtyp,"mellan: 1, 2, eller 3?")
    door = int(input())

    while 1 >= door >= 3:
        print("Du valde en dörr som inte finns, du gick in i väggen")
        points = 1
        print("Du tog en skada, försök igen")
        door = input("Välj dörr mellan: 1, 2, eller 3")

        
    if door == 1:
      print("Du valde dörr 1")

    elif door == 2:
      print("Du valde dörr 2")

    elif door == 3:
      print("Du valde dörr 3")

    else:
        while 1 >= door >= 3:
            print("Du valde en dörr som inte finns, du gick in i väggen")
            points = 1
            print("Du tog en skada, försök igen")
            door = input("Välj dörr mellan: 1, 2, eller 3")


    chans = 1 #random.randint(1,100)

    if 1 <= chans <= 33:
        monstertype = random.randint(1,3)
        monster = Monster(monstertype, regionmodifier)
        print("Bakom dörren upptäcker du ett monster, du överraskar monstret och får attackera först.")

        while monster.health > 0:
            monster.health -= player.attack
            print("Du attackerade monstret och gjorde", player.attack, "skada.")
            print("Monstret har nu", monster.health, "hp.")
            if monster.health > 0:
                print("Monstret attackerar nu dig")
                player.currenthp -= monster.attack
                print("Monstret attackerade dig och gjorde", monster.attack, "skada.")
                print("Du har nu", player.currenthp, "hp.")
                print("Det är nu din tur att attackera monstret igen.")

        print("Du dödade monstret och fick", monster.expdrop, "exp.")
        exp = exp + monster.expdrop
        while exp >= 10 + 0.1*level:
            level += 1
            hp = 5 + 2 * level
            attack = 2 + 1 * level
            if exp > 10 + 0.1*level:
                exp -= 10 + 0.1*level
            print("Du är nu level", level,".")




        





    rumsnummer += 1

        
