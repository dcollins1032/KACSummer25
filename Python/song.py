'''
Song Assignment
Dave Collins
https://github.com/dcollins1032/Python/blob/main/Unit%204/song.py
'''


def custom_song(name1, location, job, name2, body_part, body_part2, vehicle, number, jewelry, actionING, action):
    print(f"""{name1} has a barrow in the {location},
{name2} is the {job} in a band,
{name1} says to {name2} "girl I like your {body_part}",
And {name2} says this as she takes him by the {body_part2}...

Ob-la-di, ob-la-da
Life goes on, brah
La-la, how their life goes on
Ob-la-di, ob-la-da
Life goes on, brah
La-la, how their life goes on

{name1} takes a {vehicle} to the jeweler's store,
Buys a {number} karat golden {jewelry},
Takes it back to {name2} {actionING} at the door,
And as he gives it to her, she begins to {action}...

Ob-la-di, ob-la-da
Life goes on, brah
La-la, how their life goes on
Ob-la-di, ob-la-da
Life goes on, brah
La-la, how their life goes on

""")
    return

#Test Variables
'''
name1 = "desmond"
name2 = "molly"
location = "Marketplace"
job = "Singer"
body_part = "face"
body_part2 = "hand"
vehicle = "trolley"
number = "20"
jewelry = "ring"
actionING = "waiting"
action = "sing"
'''

if __name__ == "__main__": #main function
    print("This is a Mad Libs program.  Please give me some input...")
    #Variable Inputs
    name1 = input("Someone's First Name: ")
    name2 = input("Another First Name: ")
    location = input("A location: ")
    job = input("A job: ")
    body_part = input("A School Appropriate Body Part: ")
    body_part2 = input("Another School Appropriate Body Part: ")
    vehicle = input("A type of vehicle: ")
    number= str(input("A number: "))
    jewelry = input("A type of jewelry: ")
    actionING = input("An ING action: ")
    action = input("An action: ")

    #Jam Announcer
    print("\n\n\n\n\n~~~~~~~~~\nNow lets jam!!!!\n~~~~~~~~~~\n\n\n")
    #Sing the Ob La Di by The Beatles
    custom_song(name1, location, job, name2, body_part, body_part2, vehicle, number, jewelry, actionING, action)










