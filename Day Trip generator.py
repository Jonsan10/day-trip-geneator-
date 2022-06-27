import random



locations = ['buffalo ', 'wyoming ', 'South Dakota ' , 'rocky mountains ',]

transportation = ['town car ', 'helicopter ', 'submarine ', 'electric bike ']

restaurant = ['Paunch Burger ', 'Hell Kitchen ', 'Los Pollos Hermanos ', 'Chiles ' ]

entertaiment = ['jousting ', 'people watching ', 'paintball', 'hide-n-seek ']

answer = 'no'

print('Hello my name is Tom I will be helping you create a nice day trip. Lets first figure out where this trip will take place')


def get_destination():
    while True:
        a = random.choice(locations)
        print(a)
        answer=input('would you like to travel here? yes/no? ')
        if answer == 'yes':
            print('what a great location, now lets figure out how we will be traveling around on this trip.')
            return a
        elif answer == 'no':
            print('sorry lets see about another location') 
        else:
            print('invalid request')


def get_transportation():
   while True:
        b = random.choice(transportation) 
        print(b)
        answer=input('would you like to use this method of travel? yes/no? ')
        if answer == 'yes':
            print('what a great we will send it over, now lets figure out where we will be eating on this trip.')
            return b
        elif answer == 'no':
            print('sorry lets choose another method') 
        else:
            print('invalid request')



def get_resturants():
    while True:
        c = random.choice(restaurant)
        print(c)
        answer=input('would this fine dining establishment be good enough to eat at. yes/no ')
        if answer == 'yes':
            print('great we will make a reservation, great now lest figure out what type of entertainment is available in your area.')
            return c
        elif answer == 'no':
            print('sorry lets see if are other options we can recommend')
        else:
            print('invalid request')


def get_entertainment():
    while True:
        d = random.choice(entertaiment)
        print(d)
        answer=input('we have located a popular entertainment option for is area. would you like to . yes/no ')
        if answer == 'yes':
            print('great we hope you will enjoy your time. Now lets recap this day trip')
            return d
        elif answer == 'no':
            print('sorry lets see if are other options we can recommend')
        else:
            print('invalid request')



print(f'starting off the day trip will take place in,{get_destination()}, and our method of travel is {get_transportation()}, next the restaurant we made they reservation is at {get_resturants()} and ending the night the entertainment you made was {get_entertainment()}. Thus ending your day trip. Thank you for using the Day Trip Generator. ')