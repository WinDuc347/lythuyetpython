def opo_score_without579(ola_scores, weights):
    final_scores = []
    
    for i in range(len(ola_scores)):
        numerator = 0
        denominator = 0
        
        for j in range(len(ola_scores[i])):
            numerator+=ola_scores[i][j]*weights[j]
            denominator+=weights[j]
    
        final_scores.append(int(numerator/denominator+0.5))
        
    return final_scores

def statistics(opo_score):
    
    failed = 0
    tolerance = 0
    passed = 0
    
    for i in opo_score:
        if i <= 7:
            failed+=1
        elif i > 7 and i < 10:
            tolerance+=1
        else:
            passed+=1
    result = str(failed) + " failed, " + str(tolerance) + " tolerance and " + str(passed) + " passed the course"

    return result

def final_opo_score(opo_without, ola_score):
    
    new_list = opo_without.copy()
    
    for i in range(len(ola_score)):
        
        for j in range(len(ola_score[0])):
            
            if 5 < ola_score[i][j] <= 7:
                if opo_without[i] > 9:
                    new_list[i] = str(9) + "<-" + str(new_list[i])
                    
            elif ola_score[i][j] <= 5:
                if opo_without[i] > 7:
                    new_list[i] = 7
        

    return new_list

def evaluation():
    opo1 = opo_score_without579([[8, 10, 15], [4, 2, 1], [12, 7, 12], [17, 13, 11], [10, 8, 8]], [10, 20, 40])
    opo2 = opo_score_without579([[9, 10]], [0.5, 0.5])
    print (opo1)
    print (opo2)
    if len(opo1) == 5 and len(opo2) ==1:
        if opo1[0] == 13 and opo1[1] == 2 and opo1[4] == 8 and opo2[0] == 10:
            print("opo_score_without579 OK")
        else:
            print("opo_score_without579 not OK")
    else:
        print("opo_score_without579 has wrong size")
    stat_without = statistics(opo1)
    print(stat_without)
    if stat_without == "1 failed, 1 tolerance and 3 passed the course":
        print("statistics OK")
    else:
        print("statistics not OK")    
    final = final_opo_score(opo1, [[8, 10, 15], [4, 2, 1], [12, 7, 12], [17, 13, 11], [10, 8, 8]])
    print(final)
    if len(final) == 5:
        if final[0] == 13 and final[1] == 2 and final[2] == "9<-11" and final[4] == 8:
            print("final OK")
        else:
            print("final not OK")
    else:
        print("final has wrong size")
          
    
    
if __name__ == "__main__":
    evaluation()
    
        
        