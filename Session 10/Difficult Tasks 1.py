# RPG subsystem: check whether the next player move on a 5x5 tileset is possible, and if player
# is attacked by an enemy. Player symbol: 5, weak enemies (-50 health): 1, strong enemies
# (-100 health): 2. Possible player movement: LEFT, RIGHT, UP, DOWN (move one field on map).

def translate_move(direction):
    direction_list = [0,0]
    
    if direction == "UP":
        direction_list[0] -= 1
    elif direction == "DOWN":
        direction_list[0] += 1
    elif direction == "RIGHT":
        direction_list[1] += 1
    elif direction == "LEFT":
        direction_list[1] -= 1
    
    return direction_list

def player_move(health, position, direction, world):
    
    height = len(world)
    width = len(world[0])
    new_health = health
    new_world = world.copy()
    row = position[0] + translate_move(direction)[0]
    column = position[1] + translate_move(direction)[1]

# First determine whether move is possible. A move is not possible if adding the translation
# due to the direction to the position yields a value greater than the height/width of the world
# or a value less than 0    
    if 0 <= row < height and 0 <= column < width:
        
# Check to see if player encountered enemy 1 or enemy 2 and then reduce health
        if world[row][column] == 1:
            new_health -= 50
            
        elif world[row][column] == 2:
            new_health -= 100

# Update world
        new_world[position[0]][position[1]] = 0
        new_world[row][column] += 5
        
        

    return [new_health,[row,column],new_world] 

player_move
    
# THIS CODE IS NOT TO BE TOUCHED

def print_world(world):
    for row in world:
        print(row)
    print()

def test():
    game_world = [[0,0,0,0,0], [1,1,1,1,1], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,2]]
    player_health = 100
    player_location = [0,0]
    player_direction = "DOWN"

    # print_world(game_world)
    game_world[player_location[0]][player_location[1]] = 5
    print_world(game_world)
    print("Initial player health:", player_health)
    print()
    
    new_state = player_move(player_health, player_location, player_direction, game_world)
    
    if (new_state != None):
        game_world = new_state[2]
        player_location = new_state[1]
        player_health = new_state[0]
        print_world(game_world)
        print("Remaining player health:", player_health)
    else:
        print("Invalid move.")
    
    if (player_location == [1,0] and player_health == 50):
        print("Implementation successful")
    else:
        print("Implementation not correct")

# run the program.
test()

        