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
    print(f"\nAnd thus, the tale of {name} ends like it began, abrupt.")
else:
    print("The prompt you typed is not correct, a real shame cause now you gotta restart")