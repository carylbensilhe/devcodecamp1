import random

def day_trip():
    destination = ['hawaii' , 'paris', 'mexico']
    restaurant = ['steakhouse', 'sushi', 'italian']
    transportation = ['bus', 'car', 'plane']
    entertainment = ['dancing', 'tour', 'concert']
    chosen_destination = choose_from_category(destination, "destination")
    chosen_restaurant = choose_from_category(restaurant, "restaurant")
    chosen_transportation = choose_from_category(transportation, "transportation")
    chosen_transportation =choose_from_category(entertainment, "entertainment")
def choose_from_category (options, category):
    # random_option = random.choice(options)
    random_option = random
    response = input(f'We have chosen {random_option} for your {category}. Is that okay? Type "y" or "N": ')
    while response != 'y':
        # they did not like choice, reselect a destination
        random_option = random.choice(options)
        response = input(f'How about {random_option} instead? Type "y" or "n": ')
    print("Great, hope you enjoy it!")
    return random option