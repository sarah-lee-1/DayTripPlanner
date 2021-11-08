import random

destination = ["Morro Bay", "Laguna Beach", "Paso Robles"]
transportation = ["Car", "Train", "Bus"]
restaurant = ["Seafood", "Thai", "Steakhouse"] 
entertainment = ["Mission Tour", "Art Museum", "Winery"]

#Intro Message
print("\n    Welcome to your adventure! \n")
print("This is your suggested itinerary for today: \n")

#Random Generator
def get_random_destination(destination):
    random_destination = random.choice(destination)
    print(random_destination)
    return random_destination 

get_random_destination(destination)

def get_random_transportation(transportation):
    random_transportation = random.choice(transportation)
    print(random_transportation)
    return random_transportation 

get_random_transportation(transportation)

def get_random_restaurant(restaurant):
    random_restaurant = random.choice(restaurant)
    print(random_restaurant)
    return random_restaurant

get_random_restaurant(restaurant)

def get_random_entertainment(entertainment):
    random_entertainment = random.choice(entertainment)
    print(random_entertainment) 
    return random_entertainment 

get_random_entertainment(entertainment)

#Approve/Decline Generator Options

def check_dest_approval():
    request1 = input("Do you approve of chosen destination? ")
    while request1 != "yes" and "YES" and "Yes":
        dest = get_random_destination(destination)
        request1 = input("Do you approve of chosen destination? ")
    return dest 

check_dest_approval()

def check_transp_approval():
    request1 = input("Do you approve of chosen transportation? ")
    while request1 != "yes" and "YES" and "Yes":
        transp = get_random_transportation(transportation)
        request1 = input("Do you approve of chosen transportation? ")
    return transp 

check_transp_approval()

def check_rest_approval():
    request1 = input("Do you approve of chosen restaurant? ")
    while request1 != "yes" and "YES" and "Yes":
        rest = get_random_restaurant(restaurant)
        request1 = input("Do you approve of chosen restaurant? ")
    return rest 

check_rest_approval()

def check_ent_approval():
    request1 = input("Do you approve of chosen entertainment? ")
    while request1 != "yes" and "YES" and "Yes":
        ent = get_random_entertainment(entertainment)
        request1 = input("Do you approve of chosen entertainment? ")
    return ent  

check_ent_approval()


final_destination = check_dest_approval() 

final_transportation = check_transp_approval() 

final_restaurant = check_rest_approval()

final_entertainment = check_ent_approval()

def final_itinerary():
    print("\nHere is your confirmed itinerary: ") 

    print(f'{final_destination}') 

    print(f'{final_transportation}')

    print(f'{final_restaurant}')   

    print(f'{final_entertainment}')   


final_itinerary() 
