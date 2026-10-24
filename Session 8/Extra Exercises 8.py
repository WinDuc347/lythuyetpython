# FUNCTION DEFINITIONS

def total_duration(minutes):
    total = 0
    for i in minutes:
        total+=i
    return total

def average_task_length(minutes):
    average = total_duration(minutes)/len(minutes)
    return average
    
def compare_to_average(minutes):
    new_list = []
    for i in minutes:
        if i > average_task_length(minutes):
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

def task_starts_with_letter(task, letter):
    if task[0] == letter:
        return True
    return False

def find_tasks_of_type(tasks, category):
    new_list = []
    for i in tasks:
        if task_starts_with_letter(i, category):
            new_list.append(i)
    return new_list

def be_productive(tasks, minutes, available_time):
    longest_time = 0
    longest_task = ""
    i = 0
    while i < len(tasks):
        if minutes[i] > longest_time and minutes[i] <= available_time:
            longest_time = minutes[i]
            longest_task = tasks[i]
        i+=1
    
    return longest_task
    
 
 
 
# MAIN

the_tasks = ["clean_room", "clean_kitchen", "study_programming", "study_maths", "work_out"]
the_minutes = [45,60,90,75,50]

print(total_duration(the_minutes))
print(average_task_length(the_minutes))
print(compare_to_average(the_minutes))
print(task_starts_with_letter("clean room", "c"))
print(find_tasks_of_type(["clean_room", "clean_kitchen", "study_programming", "study_maths",
"work_out"],"c"))
print(be_productive(["clean_room", "clean_kitchen", "study_programming", "study_maths",
"work_out"],[35,16,18,90,60], 70))