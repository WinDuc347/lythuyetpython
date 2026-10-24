def calc_Fine(percentage):
    if percentage < 0.5:
        print("No fine.")
    elif percentage >= 0.5 and percentage <= 0.8:
        print("€50 fine.")
    elif percentage > 0.8 and percentage <= 1.5:
        print("€", int(50+1000/7*percentage+1), "fine.")
    elif percentage > 1.5:
        print("€250 fine, critical condition.")
    else:
        print("Error - Value Invalid.")

calc_Fine(1)