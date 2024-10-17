#starting information/game start screen
print("Welcome to the Game!")
print("to get started, what is your name?")
get_name = input("")
name = get_name
input("What is your blood type?: ")
print("I don't really care about your blood type, but story time now")

print(f"\n*Ahem*, okay {name}, you wake up in a strange room.")
print("you have no memory of being here or any idea why.")
print("You see a single door in front of you. Do you enter?")
print("\nChoices: 'yes' or 'no'")
first_choice = input("> ")

#first level response
if first_choice == 'yes':
    print("You choose to open the door.")
    print("As you walk through the door, you notice that you are now inside of")
    print("a brilliantly furnished living room with chairs, paintings, and a table.")
    print("On the table sits two buttons, one gold and one red. Do you press one?")
    print("\nChoices: 'yes' or 'no")
    
    button_choice = input("> ")

    #button choice
    if button_choice == 'yes':
        print("you approach the two buttons. Which will you press?")
        print("\nChoices: 'gold' or 'red")
        button_press = input("> ")
        
        #red or yellow
        if button_press == 'gold':
            print("you press the gold button")
            print("Nothing happens...weird.")
            print("until something does happen. And by something, I mean the room explodes.")
            print(f"\nAnd thus ends the tale of {name}. Perhaps all that glitters is not gold after all.")
       
        elif button_press == 'red':
            print("you press the red button.")
            print("Suddenly, the lights in the room go out. it's pitch black.")
            print("Then suddenly, the lights turn on again, but you notice the room is not like it was before.")
            print("instead of a neatly furnished space, you see that the walls are made of very old stone,")
            print("and the furniture has been replaced by rusted chains and overgrown roots.")
            print("Where the table once stood, you now see a skeleton warrior blocking a door!")
            print("The skeleton has a mighty sword. It looks ready to fight! What do you do?")
            print("\nChoices: 'talk to it', 'charge at it', 'observe surroundings'")
            skeleton_battle_start = input("> ")

            #Start of skeleton battle
            if skeleton_battle_start == 'talk to it':
                print("You try talking to the skeleton in an attempt to calm it down.")
                print("By the time you finish introducing yourself, it cuts your head clean off.")
                print("Everything goes dark, and you die")
                print(f"\nAnd thus ends the tale of {name}. I guess skeletons don't speak english.")
            
            elif skeleton_battle_start == 'charge at it':
                print("You run straight at the skeleton, slamming into it's hollow body.")
                print("You knock the skeleton off balance, but not for long. You need a follow up attack, quick!")
                print("You could try taking the sword from it. You could also try kicking it's leg out.")
                print("Of course, punching it is always an option.")
                print("What do you do?")
                print("\nChoices 'take his sword', 'kick his leg', 'punch head'")
                battle_charge_finish = input("> ")

                #End of charging route
                if battle_charge_finish == 'take his sword':
                    print("You move close, and attempt to take it's sword while it's off balance.")
                    print("The grip on the blade is firm, but you have muscles and break the hold.")
                    print("Now wielding the blade, you swing it straight down, splitting it's skull.")
                    print("The skeleton collapses, and stops moving.")
                    print("Standing triumphant, you hear the door open, a shining light behind it.")
                    print("You walk through the door, straight to your freedom, sword in hand.")
                    print(f"\nAnd thus ends the tale of {name}, the Warrior...Congrats, you win!")

                elif battle_charge_finish == 'kick his leg':
                    print("You kick out it's leg with a quick sweep, and it falls to the ground.")
                    print("As the mighty foe hit's the stone, his body shatters, crumbling into pieces.")
                    print("The door it was guarding now opens slowly, a bright light shines behind it.")
                    print("You walk through the door, straight to your freedom.")
                    print(f"\nAnd thus ends the tale of {name}, the genius fighter...Congrats, you win!")

                elif battle_charge_finish == 'punch head':
                    print("You swing at it's skull.")
                    print("As your fist makes contact, you hear a cracking of bone, your hand bone to be precise.")
                    print("As you reel in pain, the skeleton adjusts itself back, and swings it's blade.")
                    print("You feel your legs give out as you realize you have been sliced in half.")
                    print("Everything goes dark, and you die.")
                    print(f"\nAnd thus ends the tale of {name}. Little fun fact, but hands actually aren't designed for punching.")
                    print("But you probably have figured that out by now.")

                
                else:
                    print("The prompt you typed is not correct, a real shame cause now you gotta restart")
            
            elif skeleton_battle_start == 'observe surroundings':
                print("You take a step back and observe your surroundings, looking for anything you can use.")
                print("You don't see much around that you can use, save for an iron chain, a plank of wood, and a loaded gun.")
                print("Quick, what do you grab?")
                print("\nChoices: 'grab chain', 'grab plank', 'grab gun'")
                battle_observe_finish = input("> ")

                #End of observing route
                if battle_observe_finish == 'grab chain':
                    print("You grab the iron chain, and swing it at the skeleton like a mighty whip.")
                    print("But if history has taught you anything, whips only really work on beings with flesh.")
                    print("The skeleton, shaking off the strike from the chain, stabs you.")
                    print("Everything goes dark, and you die.")
                    print(f"\nAnd thus ends the tale of {name}. You picked the chain over the gun...idk man.")
                    print("I mean, I know this game kinda throws you for loops and all that but really? This was on you.")

                elif battle_observe_finish == 'grab plank':
                    print("You grab the wooden plank, and prepare for a duel.")
                    print("You clash, parry, slash, thrust, and weave with the skeleton in an epic battle.")
                    print("It's so epic, that you win the fight! yay!")
                    print("The door is open, a shining light behind it.")
                    print("You walk through the door, too your freedom.")
                    print(f"\nAnd thus ends the tale of {name}, the epic swordsman...Congrats, you win!")

                elif battle_observe_finish == 'grab gun':
                    print("You grab the gun, an obvious choice.")
                    print("But it's obvious for a reason, because you shoot clean through it's skull.")
                    print("Even the undead can't do anything a bullet. It falls to the ground")
                    print("The door it was gurading opens, a shining light behind it.")
                    print("You walk through the door, to your freedom.")
                    print(f"\nAnd thus ends the tale of {name}. You gunned down someone...congrats, you win!")

                else:
                    print("The prompt you typed is not correct, a real shame cause now you gotta restart")
            
            else:
                print("The prompt you typed is not correct, a real shame cause now you gotta restart")
       
        else:
            print("The prompt you typed is not correct, a real shame cause now you gotta restart")
    
    elif button_choice == 'no':
        print("You choose not to press a button, your indecisiveness preventing")
        print("you from ever moving forwards.")
        print("you spend the rest of your life sitting, staring at the same place forever.")
        print("You die, never really acomplishing much.")
        print(f"\nAnd thus, ends the tale of {name}. Very forgettable.")
    else:
        print("The prompt you typed is not correct, a real shame cause now you gotta restart")


elif first_choice == 'no':
    print("Really? You choose to do nothing? Alright then.")
    print(f"{name} does not open the door, almost as if to test what would happen.")
    print("But nothing ever does happen. You sit and wait until death comes, and it does.")
    print(f"\nAnd thus, the tale of {name} ends like it began, abrupt and boring.")
else:
    print("The prompt you typed is not correct, a real shame cause now you gotta restart")