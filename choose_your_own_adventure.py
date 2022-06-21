from sys import exit
 
def portal_part():
    print("The opening led you and your friend to a portal. The portal will lead you home BUT only one of you can go through it.")
    print("Do you:\n 1. Go into the portal and leave your friend behind\n 2. Leave your friend go home and possibly be lost forever")
    
    while True:
        choice = input("> ")
    
        if choice == "1":
            print("How rude! You should never leave a soldier behind.\n The portal led to the middle of nowhere. You are even more lost than before.\n Game Over!")
            exit()
        elif choice == "2":
            print("You try to find a new way out and end up finding a tunnel that leads to a small room.")
            print("""
            In this room, in order to escape the forest safe, you must choose a number between 1-10.
            If you choose the correct number you win but if you don't, you will be lost in the forest forever.
            """)
            print("Choose your number from 1-10")
            choice = input("> ")
            if choice == "7":
                print("Congrats! You guessed right.\n A helicopter showes up and brings you to safety.\n You Win!")
                exit(0)
            else:
                print("You guessed wrong.\n You never escape the dark forest and are lost forever.\n Game over.")
                exit(0)
        else:
            print("Not an option, try again.")

def weird_car():
    print("""
        After eating a nice helping of pasta with the witch, you and your friend leave the old hag behind and see a strange car light ahead.
        The two of you start to have hope and run toward the abandoned vehicle.
        You both get into the car and surprisingly the car starts.
        The only problem is that the car fuel tank is only about a quarter full. You look outside and see a jerrycan.
        Just as you were about to exit the car and retrieve the fuel, you hear something russeling in the darkness that surrounds you.
        You can't help but think that this is the same unknown creatre from the place you started.
        """)
    print("Do you\n 1. go get the fuel\n 2. Drive away and take your chances in the car.\n(Type the number that matches the choice)")

    while True:
        choice = input("> ")

        if choice == "1":
            print("\nAs you leave the car to get the jerrycan, the russling gets louder and as you reach for the fuel a deer runs by you. You feel relieved and fuel up the car and drive to safety.")
            print("Congrats you win!")
            exit(0)
        elif choice == "2":
            dead("""
            You begin to drive away and all of a sudden the car stops. OH NO! You ran out of fuel. You look towards your friend and see a figure behind them.
            Your friend is dragged out of the car. Paralyzed by fear, you don't move. The figure returns and you are dragged into the darkness and are never seen again.""")
        else:
            print("That is not an option, try again.")

def left_path():
    print("""
    As you and your friend hike down the left path, you encounter a clearing in the forest.
    In the middle of the clearing, there is a table. While approaching the table you see a phone. The phone rings and you pick up.
    The person on the other end of the line says you must answer a riddle correctly and you shall be rewarded. However, answer incorrectly and there will be concequences.\n
    The riddle is: "The more of this there is, the less you see. What is it?"
    """)
    print("What is your answer? (If you want to turn back type \"go back\")")
    
    choice = input("> ")

    if "darkness" in choice:
        print("CORRECT! I guess you will live to see another day.")
        print("\nClose by an opening in the floor becomers visible.")
        print("Do you\n 1. Go into the opening\n 2. Continue walking")
        while True:
            choice = input("> ")

            if choice == "1":
                portal_part()
            elif choice == "2":
                print("You walk around for hours and somehow end up right where everything began.")
                start()
            else:
                print("Not an option, try again.")
    elif "go back" in choice:
        print("You run back to where you came from.")
        start()
    else:
        dead("Your wrong. The floor beneath you opens up and you and your friend fall into a never ending hole.")

def right_path():
    print("""
          As the two of you wander down the right path you approach what looks to be an abandoned hut.
          You anxiously approach the structure and knock on the door.
          For a while, nothing happens. However, all of a sudden you hear a russeling sound coming from inside.
          The door swings open and an little old lady appears.
          The old lady is upset that you have interupted her sugo Sunday.
          She says that to continue on, you and your friend must answer her riddle. 
          """)
    print("The old woman asks, \"What gets wet while drying?\"")
    print("What is your answer? (If you want to turn back type \"go back\")")
    choice = input("> ")
    
    if "towel" in choice:
        print("You're right! continue on. But BEWARE of what lies ahead.")
        weird_car()
    elif "go back" in choice:
        print("You run back to where you came from.")
        start()
    else:
        dead("""
        The old woman reveals she is a witch and turns you into an apple.
        At first you may not think this is bad. However, your friend loves apples and can't resist a tasty honey crisp.
        """)

def dead(why):
    print(why, "\n You have died.\n Game Over!")
    exit(0)

def start():
    print("""
          You and your best friend wake up confused in a dark and eerie forest. 
          It feels as if someone is stalking you from afar. 
          You and your friend decide not to stick around to find out what this unknown thing is.
          As you walk through the dense forest, you approach a break in the path.
          """)
    print("Where do you decide to go? (left or right)")
    
    choice = input("> ")
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        dead("""
        You and your friend continue to argue about the path you should take. 
        During this time the unknown being creeps up behind you and emerges from the darkness.
        You open your mouth to speak.
        BAM!
        """)

start()