def F_to_C(temp):
    converted = (temp - 32)/1.8
    return converted

def alert_user(temp):
    if temp > 100:
        print("Water is boiling.")
    elif temp >= 85 and temp <= 90:
        print("Ready to make tea.")
    elif temp >= 40 and temp <= 45:
        print("Perfect for a foot bath.")
    else:
        print("The water is currently ", int(temp + 0.5), "°C.")

temp = 100

c_temp = F_to_C(temp)

alert_user(c_temp)