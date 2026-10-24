# FUNCTION DEFINITIONS
# you may write extra helper functtios HERE if you need them

''' Small example of how to use the given column names from the MAIN (see below) '''
def print_names(pokemon):   # pass the (2D) list of all pokemon as parameter
    for pkmn in pokemon:    # iterate over all individual pokemon (one pkmn is one 12-element list)
        print(pkmn[NUMBER], pkmn[NAME])   # print only the correct column/element: names are in the second column,
                            # or thus the column with index 1 (see MAIN below: NAME = 1)

def find_by_name(pokemon, name):
    '''
    Finds a pokemon by name, if it is in the list
            Parameters:
                    pokemon (list of list(s)): list of pokemon, every pokemon is a list of 12 values,
                        each pokemon has a unique name
                    name (string): name to search on
            Returns:
                    one pokemon (list): returns the pokemon (= list of 12 values) with the given name, if
                    no such pokemon is available, an empty list is returned
    '''
    # YOUR CODE HERE
    for pkmn in pokemon:
        if name == pkmn[NAME]:
            return pkmn
    return []

def find_field_by_name(pokemon, name, field):
    '''
    Finds a field of a Pokémon by its name, if it is in the list. 
            Parameters:
                    pokemon (list of list(s)): list of pokemon, every pokemon is a list of 12 values,
                        each pokemon has a unique name
                    name (string): name to search on
                    field (int): number from 0 to 11, field to find. Numbers outside of this range are
                        set to 1 (= NAME) 
            Returns:
                    the value of the desired field (int, string or booleand)
                    None, if the pokémon is not in the list
    '''
    # YOUR CODE HERE
    for pkmn in pokemon:
        if name == pkmn[NAME]:
            if field>=0 and field<=11:
                return pkmn[field]
            else:
                return pkmn[1]
    return None

def find_best(pokemon, stat):
    '''
    Finds the best pokemon, based on 'stat' in a list
            Parameters:
                    pokemon (list of list(s)): list of pokemon, every pokemon is a list of 12 values
                    stat: number from 4 to 10, selects which stat to search on. Numbers outside of this
                        range are rounded to the nearest integer within the range
            Returns:
                    name (string): the name of the pokemon who has the highest score in the selected stat
    '''
    # YOUR CODE HERE
    value = 0
    best = []
    if stat>10:
        stat=10
    elif stat<4:
        stat=4

    for pkmn in pokemon:
        if pkmn[stat] > value:
            value = pkmn[stat]
            best = pkmn
            
    return best[1]

def print_hall_of_fame(pokemon):
    '''
    Prints to the Shell an overview of the best pokemon per stat
            Parameters:
                    pokemon (list of list(s)): list of pokemon, every pokemon is a list of 12 values
            Returns:
                    nothing, prints to Shell
    '''
    # YOUR CODE HERE
    stats = ["total","HP","ATK","DEF","SP.ATK","SP.DEF","SPEED"]
    print("Hall of Fame:") 
    for i in range(len(pokemon)):
        if i >= 7:
            break
        print(stats[i], ": ", find_best(pokemon, 4+i))

        
def calc_damage(pokemon, attacker, defender):
    '''
    Returns the amount of damage done by an attack from the attacker to the defender.
    Formule: (attack of attacker times two) minus (defense of defender)
            Parameters:
                    pokemon (list of lists): list of all pokemon
                    attacker (string): unique name of attacking Pokémon
                    defender (string): unique name of defending Pokémon
            Returns:
                    damage (int): calculate using the formula, however, at least 1 damage must be dealt
                    each time this function is called
    '''
    # YOUR CODE HERE
    attack = find_field_by_name(pokemon, attacker, 6)
    defense = find_field_by_name(pokemon, defender, 7)
    
    damage = 2*attack - defense
    
    if damage < 1:
        damage = 1
    
    return damage

def is_super_effective(pokemon, attacker, defender):
    '''
    Returns True if the attack from an attacker on a defender is super effective. Use only 'type1' of a Pokémon to
    determine super effectiveness.
    Attacks from Fire on Grass are super effective.
    Attacks from Grass on Water are super effective.
    Attacks from Water on Fire are super effective.
            Parameters:
                    pokemon (list of lists): list of all pokemon
                    attacker (string): unique name of attacking Pokémon
                    defender (string): unique name of defending Pokémon
            Returns:
                    (boolean)
    '''
    attacker_type1 = find_field_by_name(pokemon, attacker, 2)
    defender_type1 = find_field_by_name(pokemon, defender, 2)
    
    if attacker_type1 == "Fire" and  defender_type1 == "Grass":
        return True
    elif attacker_type1 == "Grass" and  defender_type1 == "Water":
        return True
    elif attacker_type1 == "Water" and  defender_type1 == "Fire":
        return True
    
    return False

def is_special_attacker(pokemon, name):
    '''
    Returns True if the pokemon with the given name has a higher special attack value than attack value.
    You may assume that one Pokémon will always have different values for these stats.
            Parameters:
                    pokemon (list of lists): list of all pokemon
                    name (string): unique name of the Pokémon
            Returns:
                    (boolean)
    '''
    # YOUR CODE HERE
    sp_attack = find_field_by_name(pokemon, name, 8)
    attack = find_field_by_name(pokemon, name, 6)
    
    if sp_attack > attack:
        return True
    return False

def complex_damage(pokemon, attacker, defender):
    '''
    Returns the amount of damage done by an attack from the attacker to the defender,
    taking multiple factors in account.
    1. The attacker will always use his force to the fullest. If his attack is greater than
       his special_attack, the base formula remains:
           (attack of attacker times two) minus (defense of defender)
       If, however, his special_attack is greater that his attack, the formula becomes:
           (special_attack of attacker times two) minus (special_defense of defender)
    2. If the attacker has super effective advantage over the defender, the total damage is doubled,
       no matter the formula used for its calculation.
            Parameters:
                    pokemon (list of lists): list of all pokemon
                    attacker (string): unique name of attacking Pokémon
                    defender (string): unique name of defending Pokémon
            Returns:
                    damage (int): at least 1 damage must be dealt each time this function is called
    '''
    # YOUR CODE HERE
    effective = is_super_effective(pokemon, attacker, defender)
    special = is_special_attacker(pokemon, attacker)
    damage = calc_damage(pokemon, attacker, defender)
    
    if special:
        damage = 2*(find_field_by_name(pokemon, attacker, 8)) - (find_field_by_name(pokemon, defender, 9))
    
    if effective:
        damage*=2
    return damage
        



#_______________________________________________________________
# MAIN
# DO NOT CHANGE ANYTHING BELOW THE LINE

# a pokémon is defined by a list of 12 values
# look at 'print_names' to see how to use the following variables
# as a way to access the correct column in a readable way.
NUMBER = 0
NAME = 1
TYPE1 = 2
TYPE2 = 3
TOTAL = 4
HITPOINTS = 5
ATTACK = 6
DEFENSE = 7
SPECIAL_ATTACK = 8
SPECIAL_DEFENSE = 9
SPEED = 10
LEGENDARY = 11
#_______________________________________________________________________________________________________________






# TEST CODE: DO NOT CHANGE ANYTHING BELOW THE LINE
#________________________________________________________________________________________________________________
def test():
    
    pokemon = [ 
    #   nr.   name           type1      type2      total  HP   ATK  DEF  SP.ATK  SP.DEF  SPEED  Legendary?
        [1,   "Bulbasaur",   "Grass",   "Poison",  318,   45,  49,  49,  65,     65,     45,    False],
        [2,   "Ivysaur",     "Grass",   "Poison",  405,   60,  62,  63,  80,     80,     60,    False],
        [3,   "Venusaur",    "Grass",   "Poison",  525,   80,  82,  83,  100,    100,    80,    False],
        [4,   "Charmander",  "Fire",    "",        309,   39,  52,  43,  60,     50,     65,    False],
        [5,   "Charmeleon",  "Fire",    "",        405,   58,  64,  58,  80,     65,     80,    False],
        [6,   "Charizard",   "Fire",    "Flying",  534,   78,  84,  78,  109,    85,     100,   False],
        [7,   "Squirtle",    "Water",   "",        314,   44,  48,  65,  50,     64,     43,    False],
        [8,   "Wartortle",   "Water",   "",        405,   59,  63,  80,  65,     80,     58,    False],
        [9,   "Blastoise",   "Water",   "",        530,   79,  83,  100, 85,     105,    78,    False],
        [10,  "Caterpie",    "Bug",     "",        195,   45,  30,  35,  20,     20,     45,    True]
        ]
    
    result = 0
    # Test 0: print all names
    print_names(pokemon)
    print()
    print()
    print() # some space before the actual tests run
    
    # Test 1: find pokemon by name
    pkmn1 = find_by_name(pokemon, "Charmeleon")
    pkmn2 = find_by_name(pokemon, "Rubynator")
    if(pkmn2==[] and pkmn1==[5,"Charmeleon","Fire","",405,58,64,58,80,65,80,False]):
        result += 2
        print("Test 1 succeeded")
    
    # Test 2: find field by name
    val1 = find_field_by_name(pokemon, "Charmeleon", TOTAL)
    val2 = find_field_by_name(pokemon, "Caterpie", LEGENDARY)
    val3 = find_field_by_name(pokemon, "Wartortle", NAME)
    val4 = find_field_by_name(pokemon, "Rubynator", HITPOINTS)
    val5 = find_field_by_name(pokemon, "Caterpie", 123)
    if(val1 == 405 and val2 == True and val3 == "Wartortle" and val4 == None and val5 == "Caterpie"):
        result += 5
        print("Test 2 succeeded")
    
    # Test 3: find best pokemon per stat
    best1 = find_best(pokemon, ATTACK)
    best2 = find_best(pokemon, SPECIAL_DEFENSE)
    best3 = find_best(pokemon, 2) # 2 -> 4 -> TOTAL
    best4 = find_best(pokemon, 123) # 123 -> 10 -> SPEED
    if(best1=="Charizard" and best2=="Blastoise" and best3=="Charizard" and best4=="Charizard"):
        result += 4
        print("Test 3 succeeded")
        
    # Test 3 bis: print hall of fame
    print_hall_of_fame(pokemon)
    
    # Test 4: calc damage
    dam1 = calc_damage(pokemon, "Blastoise", "Charizard")
    dam2 = calc_damage(pokemon, "Charizard", "Blastoise")
    dam3 = calc_damage(pokemon, "Caterpie", "Blastoise")
    if(dam1 == 88 and dam2 == 68 and dam3 == 1):
        result += 3
        print("Test 4 succeeded")
        
    # Test 5: super effective
    test1 = is_super_effective(pokemon,  "Blastoise", "Charizard")
    test2 = is_super_effective(pokemon,  "Charizard", "Caterpie")
    if(test1 == True and test2 == False):
        result += 2
        print("Test 5 succeeded")
        
    # Test 6: special attacker
    sp_atk1 = is_special_attacker(pokemon, "Charizard")
    sp_atk2 = is_special_attacker(pokemon, "Caterpie")
    if(sp_atk1 == True and sp_atk2 == False):
        result += 2
        print("Test 6 succeeded")
        
    # Test 7.1: complex damage: atk, not super effective
    comp1 = complex_damage(pokemon, "Caterpie", "Caterpie")
    if(comp1 == 25):
        result += 1
        print("Test 7.1 succeeded")
    # Test 7.2: complex damage: low damage
    comp2 = complex_damage(pokemon, "Caterpie", "Charizard")
    if(comp2 == 1):
        result += 1
        print("Test 7.2 succeeded")
    # Test 7.3: complex damage: sp_atk, not super effective
    comp3 = complex_damage(pokemon, "Squirtle", "Caterpie")
    if(comp3 == 80):
        result += 1
        print("Test 7.3 succeeded")
    # Test 7.4: complex damage: sp_atk, super effective
    comp3 = complex_damage(pokemon, "Squirtle", "Charizard")
    if(comp3 == 30):
        result += 1
        print("Test 7.4 succeeded")

    print("Total result : ", result, "/22")

if __name__ == "__main__":
    test()