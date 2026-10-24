def print_multiples(to):
    for i in range(1, to+1):
        for j in range(1, 11):
            print(i*j, end = "\t")
        print("")
        
print_multiples(6)