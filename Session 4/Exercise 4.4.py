import random # needed for heal function, see lab text

### Function Definitions ###
def attack_is_valid(attack):
    # Your code here
    
    if attack > 0:
        return True
    
    return False

def defense_is_valid(attack, defense):
    # Your code here
    
    if defense > 0 and defense <= attack:
        return True
    
    return False

def calc_damage(attack, defense, is_critical):
    # Your code here
    
    damage = attack - defense
    
    if defense >= attack:
        damage = 1
    
    if is_critical:
        return damage*2
    
    return damage

def calc_hitpoints(damage, current_hitpoints):
    # Your code here
    
    hitpoints = current_hitpoints - damage
    
    if hitpoints <= 0:
        return "Target has fainted"
    else:
        return ("Target has " + str(hitpoints) + " hitpoints left")
    
def heal(current_hitpoints, max_hitpoints):
    # Your code here
    
    if max_hitpoints - current_hitpoints >= 10:
        return random.randint(1, 10)
    
    return 0

### Main Program: Don't change anything below this line! ###
#___________________________________________________________
final_grade = 0

attack_pikachu = 25
defense_pikachu = 5
attack_caterpie = 10
defense_caterpie = 10
attack_charizard = 0
defense_charizard = 50
attack_mewtwo = -9


print("Test 1: attack_is_valid...")
if ((attack_is_valid(attack_pikachu) == True) and (attack_is_valid(attack_caterpie) == True) and (attack_is_valid(attack_mewtwo) == False) and (attack_is_valid(attack_charizard) == False)):
    final_grade = final_grade + 4
    print("Test 1 OK")
else:
    print("Test 1 FAILED")


print("Test 2: defense_is_valid...")
if ((defense_is_valid(attack_pikachu, defense_pikachu) == True) and (defense_is_valid(attack_caterpie, defense_caterpie) == True) and (defense_is_valid(attack_charizard, defense_charizard) == False)):
    final_grade = final_grade + 4
    print("Test 2 OK")
else:
    print("Test 2 FAILED")
  
  
print("Test 3: calc_damage...")
damage1 = calc_damage(attack_caterpie, defense_pikachu, False)
damage2 = calc_damage(attack_caterpie, defense_charizard, False)
damage3 = calc_damage(attack_pikachu, defense_caterpie, True)
if(damage1 == 5 and damage2 == 1 and damage3 == 30):
    final_grade = final_grade + 4
    print("Test 3 OK")
else:
    print("Test 3 FAILED")


print("Test 4: calc_hitpoints...")
hp1 = calc_hitpoints(20, 10)
hp2 = calc_hitpoints(18, 18)
hp3 = calc_hitpoints(9, 11)
hp4 = calc_hitpoints(16, 36)
if(hp1 == "Target has fainted" and hp2 == "Target has fainted" and hp3 == "Target has 2 hitpoints left" and hp4 == "Target has 20 hitpoints left"):
    final_grade = final_grade + 4
    print("Test 4 OK")
else:
    print("Test 4 FAILED")


print("Test 5: heal...")
heal1 = heal(30, 20)
heal2 = heal(18, 18)
heal3 = heal(10, 20)
if(heal1 == 0 and heal2 == 0 and heal3 > 0 and heal3 <= 10):
    final_grade = final_grade + 4
    print("Test 5 OK")
else:
    print("Test 5 FAILED")


print("Your score for this exercise is ", final_grade, "/20.")