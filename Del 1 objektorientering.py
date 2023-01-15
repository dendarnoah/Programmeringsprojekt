import random
import time
level = 1
exp = 0
strength_bonus = 0
hp = round(5 + 2*level)
attack = round(2 + 1*strength_bonus)


class Player():
    def __init__(self, name):
        self.name = name
        self.health = hp
        self.level = level
        self.exp = exp
        self.attack = attack

    def exp(self):
        self.exp + expdrop
        while exp >= 20 + 0.2*level:
            level += 1
            hp = 5 + 2 * level
            attack = 2 + 1 * strength_bonus
            if exp > 20 + 0.2*level:
                exp -= 20 + 0.2*level
            print("Du är nu level", level,".")


class Monster():
    def __init__(self, monstertype):
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
            
        self.health = round(self.health + 0.1 * level)
        self.attack = round(self.attack + 0.1 * level)
        
    def damage(self):
        playerattack
        self.health -= playerattack
        print("Monstret har efter din attack", monster.health, "hp")

    def get_health(self):
        print(self.health)

    def get_level(self):
        print(level)


class Chest():
    def __init__(self, chesttype):
        self.type = chesttype

        if chesttype == 1:
            random_item = random.randint(1, 100)
            if random_item == 1:
                item = 6
            elif random_item == 2:
                item = 5
            elif 3 <= random_item <= 17:
                item = 4
            elif 18 <= random_item <= 32:
                item = 3
            elif 33 <= random_item <= 64:
                item = 2
            elif 65 <= random_item <= 100:
                item = 1
            self.item = item
            self.expdrop = 2

        elif chesttype == 2:
            random_item = random.randint(1, 100)
            if random_item == 1:
                item = 1
            elif random_item == 2:
                item = 2
            elif 3 <= random_item <= 17:
                item = 3
            elif 18 <= random_item <= 32:
                item = 4
            elif 33 <= random_item <=64:
                item = 5
            elif 65 <= random_item <= 100:
                item = 6
            self.item = item
            self.expdrop = 5



class Item():
    def __init__(self, itemtype):
        self.type = itemtype
        if itemtype == 1:
            self.strengthmod = 10
            self.name = "Härskarringen"
        if itemtype == 2:
            self.strengthmod = 9
            self.name = "Det heliga halsbandet"
        if itemtype == 3:
            self.strengthmod = 7
            self.name = "Det heliga armbandet"
        if itemtype == 4:
            self.strengthmod = 4
            self.name = "Magiskt halsband"
        if itemtype == 5:
            self.strengthmod = 2
            self.name = "Magiskt armband"
        if itemtype == 6:
            self.strengthmod = 1
            self.name = "Magisk ring"

    def __str__(self):
        return f"{self.name} (strength modifier: {self.strengthmod})"


inventory = []

def add_item(item):
    global strength_bonus
    if len(inventory) < 5:
        inventory.append(item)
        strength_bonus += item.strengthmod
        attack = 2 + 0.2 * strength_bonus
    else:
        print("Väskan är full.")
        print("Vill du byta ut ett föremål? (ja/nej)")
        choice = input()
        while True:
            if choice == "ja":
                for i, inv_item in enumerate(inventory):
                    print(f"{i+1}. {inv_item}")
                while True:
                    print("Skriv numret på föremålet du vill byta ut.")
                    replace_index = int(input()) - 1
                    if replace_index >= 0 and replace_index < len(inventory):
                        break
                    else:
                        print("Du valde ett ogiltigt nummer, försök igen.")
                replaced_item = inventory[replace_index]
                strength_bonus -= replaced_item.strengthmod
                inventory[replace_index] = item
                strength_bonus += item.strengthmod
                break
            elif choice == "nej":
                print("Du lämnade föremålet.")
                break
            else:
                print("Ogiltigt svar, försök igen.")


# View the contents of the inventory
def show_inventory():
    for i, item in enumerate(inventory):
        print(f"{i+1}. {item}")

#monster = Monster(1)


sentence = "Du är en vilsen äventyrare som kommit långt hemifrån."
for char in sentence:
    print(char, end='', flush=True)
    time.sleep(0.02)


Karaktär = input("Välj ditt namn ->")
confirmation = input(f"Är du säker på att du vill välja {Karaktär} som ditt namn? (ja/nej)")
while confirmation.lower() != "ja":
    if confirmation.lower() == "nej":
        Karaktär = input("Välj ditt namn ->")
        confirmation = input(f"Är du säker på att du vill välja {Karaktär} som ditt namn? (ja/nej)")
    else:
        confirmation = input("Vänligen svara med ja eller nej")

poäng = 10
styrka = 0
försvar = 0
print("Du har 10 poäng att spendera")

while poäng > 0:
    styrkepoäng = int(input("Välj din styrka ->"))
    while poäng - styrkepoäng < 0 or styrkepoäng < 0:
        print("Du valde ett för högt nummer eller ett negativt nummer, vänligen välj ett nummer mellan 0 och ",poäng)
        styrkepoäng = int(input("Välj din styrka ->"))
    styrka += styrkepoäng
    poäng = poäng - styrkepoäng
    print("Du har styrkan", styrka, "Du har poängen ", poäng, "kvar att spendera")
    försvarspoäng = int(input("Välj ditt försvar ->"))
    while poäng - försvarspoäng < 0 or försvarspoäng < 0:
        print("Du valde ett för högt nummer eller ett negativt nummer, vänligen välj ett nummer mellan 0 och ",poäng)
        försvarspoäng = int(input("Välj ditt försvar ->"))
    försvar += försvarspoäng
    poäng = poäng - försvarspoäng
    print("Styrka", styrka, "försvar", försvar, "poäng", poäng)

hp = 5 + 2*level + 0.5 * försvar

player = Player(Karaktär)

sentence = "Du vandrar planlöst genom skogar och ängar i vad som känns som år. \nDu kommer tillslut fram till ett samhälle.\nDu upptäcker ganska omgående att allt inte är som det ska. \nDetta samhälle är helt tomt och det ända som återfinns av en civilisation är lik. \nI skogen intill ser du rörelse, du går fram för att undersöka.\nSå fort du når fram ser du att du kan välja mellan tre stigar, vilken väljer du?"
for char in sentence:
    print(char, end='', flush=True)
    time.sleep(0.02)

rumsnummer = 0
while level <=10:

    while rumsnummer >= 1:
        choice = input("Du kan välja mellan att visa:\n1. inventory\n 2. spelare\n 3. fortsätt\n")
        if choice == "1" or choice.lower() == "inventory":
            show_inventory()
        elif choice == "2" or choice.lower() == "spelare":
            print(round(player.health))
            print(player.level,"\n")
        elif choice == "3" or choice.lower() == "fortsätt":
            break
        else:
            print("Du valde ett ogiltigt alternativ, välj igen.")

    print("\nVälj stig mellan: 1, 2, eller 3?\n")
    door = int(input())

    if door == 1:
      print("Du valde stig 1")

    elif door == 2:
      print("Du valde stig 2")

    elif door == 3:
      print("Du valde stig 3")

    else:
        while not 1 <= int(door) <= 3:
            print("Du valde en stig som inte finns, du gick in i väggen")
            points = 1
            print("Du tog en skada, försök igen")
            door = input("Välj stig mellan: 1, 2, eller 3")


    chans = random.randint(1,100)

    if 1 <= chans <= 33:
        monstertype = random.randint(1,3)
        monster = Monster(monstertype)
        print("Bakom en buske vid stigen upptäcker du ett monster, du överraskar monstret och får attackera först.")

        while monster.health > 0:
            monster.health -= player.attack
            print("Du attackerade monstret och gjorde", player.attack, "skada.")
            print("Monstret har nu", monster.health, "hp.")
            if monster.health > 0:
                print("Monstret attackerar nu dig")
                player.health -= monster.attack
                print("Monstret attackerade dig och gjorde", monster.attack, "skada.")
                print("Du har nu", player.health, "hp.")
                print("Det är nu din tur att attackera monstret igen.")
            if player.health <= 0:
                print("Du dog.")
                print("GAME OVER!")
                exit()

        print("Du dödade monstret och fick", monster.expdrop, "exp.")
        exp = exp + monster.expdrop
        rumsnummer += 1
        while exp >= 20 + 0.2*level:
            level += 1
            hp = 5 + 2 * level
            attack = 2 + 1 * strength_bonus
            if exp > 20 + 0.2*level:
                exp -= 20 + 0.2*level
            print("Du är nu level", level,".\n")

    if 34 <= chans <= 66:
        random_chesttype = random.randint(1,10)
        if random_chesttype == 1:
            chesttype = 2
            print("Du vandrar vidare längs stigen och hittar en guldkista.")
        else:
            chesttype = 1
            print("Du vandrar vidare längs stigen och hittar en träkista.")
        chest = Chest(chesttype)
        föremål1 = Item(chest.item)
        add_item(föremål1)
        print("Du hittade ", föremål1, "Du känner någon form av magisk aura som gör dig starkare från föremålet.\nDu lägger föremålet i väskan.\n")
        exp = exp + chest.expdrop
        while exp >= 20 + 0.2*level:
            level += 1
            hp = 5 + 2 * level
            attack = 2 + 1 * strength_bonus
            if exp > 20 + 0.2*level:
                exp -= 20 + 0.2*level
            print("Du är nu level", level,".\n")
        rumsnummer += 1

    if 67 <= chans <= 100:
        print("Du klev i en fälla och tog 1 skada!")
        player.health -= 1
        print("Ditt hp är nu", player.health,".\n")
        rumsnummer += 1

        
