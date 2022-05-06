


choice_one = input("\nYou are asked to join a discord server: do you choose the MAKEUP chat or MINECRAFT chat? \n")
con = ["\nConnecting to server...", "Connecting to server...", "Connecting to server...", "Connected.\n"]

response = True

if choice_one.lower() == "makeup":
    for con in con:
        print(con)
    choice_person = input("\nThere are two different popular creators that want to chat \nwith you: do you choose JAMES CHARLES or MANNY MUA? \n")
    if choice_person.lower() == "james charles":
        choice_james = input("\nJames Charles: Hi Sister! Pick a number 1-3? ")
        if choice_james == "1":
            print("Congrats you won the chance to film a makeup tutorial with me! Bye.")
            response = False
        elif choice_james == "2":
            print("Congrats you won my James Charles Eyeshadow Palette! Bye.")
            response = False
        elif choice_james == "3":
            print("Congrats you won a free ticket to my next meet and greet! \nSee you soon Sister! Bye.")
            response = False
        else:
            response = True
    elif choice_person.lower() == "manny mua":
        print("\nManny MUA: Everyone grows at their own pace, \nand you shouldn't compare yourself to anyone.")
        print("\nMe: Thank you for those wise words bestie!!\n")
    else:
        response = True
elif choice_one.lower() == "minecraft":
    for con in con:
        print(con)
    choice_mine = input("\nThere are 2 current games going on \nthat you can join: do you join TOMMYINNIT or DREAM?\n")
    if choice_mine.lower() == "tommyinnit":
        choice_game = input("\nTommyInnIt: Hey which type of mod would you like me to add to our game: \nMUTANT enemies, RESPAWN as something new everytime, or SUPERPOWERS?\n")
        if choice_game.lower() == "mutant":
            print("\nYou got killed by a mutant creeper.\n")
        elif choice_game.lower() == "respawn":
            print("\nYou respawned as the Ender Dragon and could not complete the game.\n")
        elif choice_game.lower() == "superpowers":
            print("\nTommyinnit killed you with his extreme strength with one swing.\n")
        else:
            response = True
    elif choice_mine.lower() == "dream":
        choice_dream = input("\nDream: There are a 2 different modes we can play: \nwould you rather play SURVIVAL or CREATIVE?\n")
        if choice_dream.lower() == "survival":
            print("\nYou won the game and slayed the Ender Dragon.\n")
            response = False
        elif choice_dream.lower() == "creative":
            print("\nYou designed and created an entire village that was very elaborate.\n")
            response = False
        else:
            response = True
    else:
        response = True
else:
    response = True

if response:
    print("\nHahaha loser! Try again!\n")
else:
    print("\nMe: Thank you so much! Bye.\n")
