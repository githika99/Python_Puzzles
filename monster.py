class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.name = name
        self.type = "Normal"
        self.current_hp = int(hp)
        self.max_hp = int(hp)
        self.attacks = [["wait",0]]        
        self.possible_attacks = {"wait":0, 'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3,
                            'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'tornado': 4}
    def add_attack(self, attack_name):
        if attack_name not in self.possible_attacks:
           return False
        if len(self.attacks) == 4:
            lowest_hp_name = self.attacks[0][0]  #first name       keys[0] key
            lowest_hp = self.attacks[0][1]       #first value      keys[1]  value
            for keys in self.attacks:
                if keys[1] < lowest_hp:
                    lowest_hp_name = keys[0]
                    lowest_hp = keys[1]
                elif keys[1] == lowest_hp:
                    if keys[0] < lowest_hp_name:                #key comes first in the alphabet
                        lowest_hp_name = keys[0]
                        lowest_hp = keys[1]
            #print("called remove for", lowest_hp_name)
            self.remove_attack(lowest_hp_name)
        hp = self.possible_attacks[attack_name]
        self.attacks.append((attack_name, hp))
        #print("added", attack_name)
        return True

    def remove_attack(self, attack_name):
        hp = self.possible_attacks[attack_name]
        if [attack_name,hp] not in self.attacks:     #if tup(attack_name, value) not in self.attacks:
            #print("not removed", attack_name)
            #print((attack_name,hp))
            #print((attack_name,hp) in self.attacks)
            return False
        self.attacks.remove([attack_name, hp])
        if len(self.attacks) == 0:
            self.attacks.append(("wait", 0))

        #print("removed", attack_name)
        return True
        
    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        return None
    
    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        return None
  
def monster_fight(monster1, monster2):
    print("Monster fight function invoked")
    #edge case
    if len(monster1.attacks) == 1 and monster1.attacks[0][0] == "wait" and len(monster2.attacks) == 1 and monster2.attacks[0][0] == "wait":
        return -1, None, None
    
    monster1.attacks = sorted(monster1.attacks, key=lambda x: (x[1], x[0]))
    monster2.attacks = sorted(monster2.attacks, key=lambda x: (x[1], x[0]))
    monster1_succesful_attacks = []
    monster2_succesful_attacks = []
    
    
    counter = 0
    for keys in monster1.attacks:
        if counter > 0:
            if keys[1] == monster1.attacks[counter - 1][1]:
                if keys[0] > monster1.attacks[counter - 1][0]:
                    temp = monster1.attacks[counter]
                    monster1.attacks[counter] = monster1.attacks[counter - 1]
                    monster1.attacks[counter - 1] = temp
        counter += 1
    
    counter = 0
    for keys in monster2.attacks:
        if counter > 0:
            if keys[1] == monster2.attacks[counter - 1][1]:
                if keys[0] > monster2.attacks[counter - 1][0]:
                    temp = monster2.attacks[counter]
                    monster2.attacks[counter] = monster2.attacks[counter - 1]
                    monster2.attacks[counter - 1] = temp
        counter += 1


    print("monster ", monster1.name, " attacks: ", monster1.attacks)
    print("monster ", monster2.name, " attacks: ", monster2.attacks)
    
    rounds = 0
    monster1_attack_num = len(monster1.attacks) - 1
    monster2_attack_num = len(monster2.attacks) - 1
    
    while monster1.current_hp > 0 and monster2.current_hp > 0:      #both monsters' hps are greater than 0
        rounds += 1

        monster2.current_hp -= monster1.attacks[monster1_attack_num][1]
        monster1_succesful_attacks.append(monster1.attacks[monster1_attack_num][0])
        if monster2.current_hp <= 0:    #monster 2 lost
            break
            
        if monster1_attack_num == 0:
            monster1_attack_num = len(monster1.attacks) - 1
        else:
            monster1_attack_num -= 1
        
        monster1.current_hp -= monster2.attacks[monster2_attack_num][1]
        monster2_succesful_attacks.append(monster2.attacks[monster2_attack_num][0])
        if monster1.current_hp <= 0:    #monster 1 lost
            break
            
        if monster2_attack_num == 0:
            monster2_attack_num = len(monster2.attacks) - 1
        else:
            monster2_attack_num -= 1
        

        print("round num:", rounds, " monster 1 hp: ", monster1.current_hp, " monster 2 hp: ", monster2.current_hp)

    
    if monster1.current_hp <= 0:        #monster 1 lost
        monster1.lose_fight()
        monster2.win_fight()
        return rounds, monster2, monster2_succesful_attacks
    
    else:                       #monster 2 lost          monster2.hp <= 0
        monster2.lose_fight()
        monster1.win_fight()
        return rounds, monster1, monster1_succesful_attacks

#main
Srujana = Monster("Srujana")
Srujana.add_attack("fire_storm")
Srujana.add_attack("whirlwind")


Roshini = Monster("Roshini")
Roshini.add_attack("ice_storm")
Roshini.add_attack("whirlwind")


print(monster_fight(Srujana, Roshini))

print("NEW MONSTER FIGHTTTTT")

print(monster_fight(Roshini, Srujana))





