#Playing a game of guess my animal

color = input("Guess the color of my animal: ").lower()
if color == "grey" or color == "gray":
    print("You got it!\n")
else:
    print("Nope, it was grey...or gray if you're British.\n")
 
    
lives = input("Do you think my animal lives in the woods, desert, or the savanna? ").lower()
if lives == "savanna":
    print("Yeppers!\n")
else:
    print("Nope...savanna.\n")
    
    
fur = input("Do you think my animal has fur? ").lower()
if fur == "no":
    print("Right-O!\n")
else:
    print("No fur for my animal.\n")
    
    
animal = input("Why don't you guess what my animal is: ").lower()
if animal == "elephant":
    print("Winner!")
else:
    print("Loser! It was an elephant.")