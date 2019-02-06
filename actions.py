# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input("what is your name ")
my_age = -1
my_bio = input("tell me somthing about u ")
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    # your code goes here!
    print("would you like to :")
    print("1) create a new club")
    print("or :")
    print("2) Browse and join clubs.")
    print("or:")
    print("3) View existing clubs")
    print("or:")
    print("4) Display member of a club")
    print("or :")
    print("-1) Close application")
    chose = input(">")

    if chose == ("1"):
        create_club()
    elif chose == ("2"):
        view_clubs()
        join_clubs()
    elif chose == ("3"):
        view_clubs()
    elif chose == ("4"):
        view_club_members()
    elif chose == ("-1") :
        print("good bye")
        quit()
    else :
        options = input("invalid input")   


    

def create_club():
    # your code goes here!
    name_club = input("pick a name for your awesome new club :")
    print("what is your club about ?")
    disc_club = input("")
    new_club = Club(name_club , disc_club)
    print(" how many Persons you want to add to your club (-1 to stop)")
    print("....")
    for item in population:
        print("(%s) %s" % (population.index(item)+1, item.name))
    member = input("> ")
    while member != "-1":
        if population[int(member)-1] in population:
            new_club.recruit_member(population[int(member)-1])
            member = input("> ")
    print("here is your club")
    print(new_club.name)
    print(new_club.description)
    print("members :")
    total_age = 0
    for member in new_club.members:
        print("member name is: %s \n member age is: %s \n - %s " % (member.name , member.age , member.bio))
        print ("...")
        total_age == member.age
    avrg = float(total_age) / len(new_club.members)
    print("the average is %.2f years old " % avrg)
    clubs.append(new_club)  
    print("your %s club is created " % new_club.name)
    options()


def view_clubs():
    # your code goes here!
    for club in clubs:
        print("name : %s " % club.name)
        print("description %s" % club.description)
        print("members %s" % club.members)
        print("")
       
    

def view_club_members():
    # your code goes here!
    view_clubs()
    print("")
    user_input_club = input("chooes your club")
    opj_club = None
    for club in clubs:
        if (club.name == user_input_club):
            opj_club = club
            for member in opj_club.member:
                print("member name is: %S \n member age is: %s \n - %s " (member.name , member.age , member.bio))
    options()           

def join_clubs():
    # your code goes here!
    view_clubs()
    print("")
    user_join_club = input("join the club you want ")
    opj_club = None
    for club in clubs:
        if (club.name == user_join_club):
            opj_club = club
            opj_club.recruit_member(myself)
            break
    print("%s just join %s " % (myself.name , opj_club.name))
    options()       



def application():
    introduction()
    # your code goes here!
    
