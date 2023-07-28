import random

play = input("Do you want to play some pick-up basketball? ").lower()
if play == "no":
    print("Welp, that was fun.")
    exit()
else:
    print("")

shirt = input("Do you want a tee shirt, dri-fit, or jersey? ").lower()
if shirt == "tee shirt" or shirt == "tee":
    print("I like to play in a tee shirt!\n")
elif shirt == "dri-fit":
    print("You look good in a dri-fit!\n")
else:
    print("You gotta support your team!\n")
    

shorts = input("Do you want grey, black, or white shorts? ").lower()
if shorts == "grey":
    print("Grey is my favorite color.\n")
elif shorts == "black":
    print("Black goes with anything.\n")
else:
    print("White looks good on everyone.\n")
    
    
shoes = input("You going with Dame, Kobe, or Lebron shoes? ").lower().capitalize()
if shoes == "Dame":
    print("I love me some Dame time!\n")
elif shoes == "Kobe":
    print("Gotta love the Black Mamba!\n")
else:
    print("He is the all-time leading scorer!\n")
    

print("Let me text my friend to see if we will be playing 3 on 3, 4 on 4, or 5 on 5.")
num = random.randint(5,12)
print("There are " + str(num) + " people there.")
if num < 7:
    print("Looks like we will be playing 3 on 3.\n")
elif num < 10:
    print("Looks like we will be playing 4 on 4.\n")
else:
    print("Looks like we will be playing 5 on 5.\n")


fouls = input("Are you ok with calling your own fouls? ").lower()
if fouls == "yes":
    print("Ok, good.\n")
else:
    print("Hopefully someone brought a whistle.\n")
    
    
driving = input("Who's driving? You or me? ").lower()
if driving == "me":
    print("Your car is nicer than mine.\n")
else:
    print("Ok, let me clean all the trash off the front seat.\n")
    
    
print("Let's go!")