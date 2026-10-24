### Define functions ###

def avgScore(file_name):
    '''
    Calculate average score of all results stored in a given file.

            Parameters:
                    file_name (string): name of file where all results are stored

            Returns:
                    avg_score (int): average score of all results
    '''
    average = 0
    counter = 0
    
    file = open(file_name, "r")
    
    for line in file:
        average += int(line)
        counter += 1
        
    return average/counter

def nrScoresHigherThan(result, file_name):
    '''
    Counts all numbers that are higher than a given value.

            Parameters:
                    result (int): number that is tested, which scores should exceed
                    file_name (string): name of file where all results are stored

            Returns:
                    counter (int): total count of all scores exceeding value 'result'
    '''
    number = 0
    
    file = open(file_name, "r")
    
    for line in file:
        if int(line) > result:
            number += 1
            
    return number

def maxScore(file_name):
    '''
    Calculates the maximum score in all results.

            Parameters:
                    file_name (string): name of file where all results are stored

            Returns:
                    max (int): maximum score of all results
    '''
    score = 0
    
    file = open(file_name, "r")
    
    for line in file:
        if int(line) > score:
            score = int(line)
            
    return score
    
### Main program ###
### you do not have to alter anything after this line ###
# Read data from file
file_name_of_ct = "results.txt"

benchmark = 10
# Test functions
print("The avarege score is:", avgScore(file_name_of_ct))
print("Number of students with a higher score than", benchmark, "are:", nrScoresHigherThan(benchmark, file_name_of_ct))
print("The maximum score:", maxScore(file_name_of_ct))


