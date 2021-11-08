# * Sarah Lee 
import random


destination = ["Morro Bay", "Laguna Beach", "Paso Robles"]
restaurant = ["Seafood", "Thai", "Steakhouse"] 
transportation = ["Car", "Train", "Bus"]
entertainment = ["Mission Tour", "Art Museum", "Winery"]


def get_random_destination(destination):
    random_destination = random.choice(destination)
    print(random_destination)

get_random_destination(destination)

def get_random_transportation(transportation):
    random_transportation = random.choice(transportation)
    print(random_transportation)

get_random_transportation(transportation)


def get_random_restaurant(restaurant):
    random_restaurant = random.choice(restaurant)
    print(random_restaurant)

get_random_restaurant(restaurant)


def get_random_entertainment(entertainment):
    random_entertainment = random.choice(entertainment)
    print(random_entertainment)

get_random_entertainment(entertainment)


def check_dest_approval():
    request1 = input("Do you approve of chosen destination? ")
    while request1 != "Yes" and request1 != "yes" and request1 != "YES":
        get_random_destination(destination)
        # breakpoint()

        request1 = input("Do you approve of chosen destination? ")

    # was going to do an "If/Else" here but wanted to "simplify"
    # else:
    #     get_random_destination(destination)

check_dest_approval()
