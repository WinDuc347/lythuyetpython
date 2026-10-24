def walk_with_dog(weather, temperature):
    if weather == "Rainy":
        print("Stay at home.")
    else:
        if temperature > 25:
            print("Stay at home.")
        else:
            print("Go for a walk")
    
walk_with_dog("Sunny", 25)