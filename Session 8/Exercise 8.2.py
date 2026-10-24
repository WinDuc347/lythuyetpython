# FUNCTION DEFINITIONS
# ***  YOUR FUNCTIONS HERE  ***

#a
def num_of(plants, labels, label):
    new_list = []
    j = 0
    for i in labels:
        if i == label:
            new_list.append(plants[j])
        j+=1
    return new_list

#b
def price_tree(name):
    return len(name)*10

#c
def price_cactus(name):
    price = price_tree(name)
    if name[0]=="A" or name[0]=="E" or name[0]=="I" or name[0]=="O" or name[0]=="U":
        price*=2
    return price

#d
def price_flower(name):
    price = price_cactus(name)
    if price > 100:
        price = 100
    elif price < 40:
        price = 40
    return price

#e
def prices(plants, labels):
    new_list = []
    j = 0
    for i in plants:
        if labels[j] == "t":
            new_list.append(price_tree(i))
        elif labels[j] == "c":
            new_list.append(price_cactus(i))
        elif labels[j] == "f":
            new_list.append(price_flower(i))
        else:
            new_list.append(0)
        j+=1
        
    return new_list

#_________________________________________________________
# MAIN, you MAY change this, since you test your own code

plants = ["Aztekium", "Cereus","Melocactus","Oak","Willow","Banana","Sunflower","Rose","Orchid"]
labels = ["c","c","c","t","t","t","f","f","f"]

print(num_of(plants,labels,"t"))
print(price_tree("Oak"))
print(price_cactus("Aztekium"))
print(price_flower("Orchid"))
print(prices(["Oak", "Willow", "Orchid"],["t", "nonsense", "f"]))