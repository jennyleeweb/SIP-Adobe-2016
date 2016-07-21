print("You wake up one morning nd find that you are not in your bed; you are not even in your room. You are in the middle of a gaint maze. A sign is hanging from the ivy: 'You have one hour. Do not touch the walls.' There is a hallway to your right and to your left. Type 'left' to go left or 'right' to go right.")

user_input = input()
while user_input != ("left" or "right"): 
    user_input= input("Type 'left' to go left or 'right' to go right.")
    break
if user_input == "left":
    print("You decide to go left and are surrounded by hungry sharks.") 
    # done = True
    print("Luckily, there are two rocks you can jump over to escape. Type 'brown' to jump to the boulder or 'gray' to jump to the stone")
    rock= input()
    while rock != ("brown" or "gray"):
        rock= input("Luckily, there are two rocks you can jump over to escape. Type 'brown' to jump to the boulder or 'gray' to jump to the stone")
        break
    if rock == "brown":
        print("You escaped the sharks, and will need to hike up the mountain. You are stranded and need to get help. Type 'fire' to light a fire or 'stay' to live on the mountain forever.")
        help_signal= input()
        while help_signal != ("fire" or "stay"):
            help_signal = input("You are stranded and need to get help. Type 'fire' to light a fire or 'stay' to live on the mountain forever.")
        if help_signal == "fire":
            print("The President flies by in an airplane and sees your fire. He orders the pilot to land and rescues you out. Congratualtions!")
        elif help_signal== "stay": 
            print("You find goats on the mountain and tame them. They become your loving pets and milk source and you live happily as a mountainman.")
    elif rock == "gray":
        print("You befriend the sharks and they offer you two choices- to ride home on them or ask their sea god for a wish. Type 'ride' to ride the sharks home or 'sea god' to be granted a wish.")
        choice= input()
        while choice != ("ride" or "sea god"):
            choice= input("Type 'ride' to ride the sharks home or 'sea god' to be granted a wish.")
            break
        if choice == "ride": 
            print("The sharks prove their loyalty and give you a thrilling ride home without eating you! You ask for their number and keep in touch with your new shark friends.")
        elif choice == "sea god":
            print("The sea god is annoyed, but answers the sharks\' call. He does not give you choice of a wish but will send you home safely. You become a devoted sea god worshipper and live a fulfilling beach life.")
elif user_input == "right":
    print("You choose to go right and a scamming merchant follows you around. Luckily, there are two plants you can wait him out in. Type 'bush' to hide im the bush or 'tree' to hide in the tree") # finished the story writing what happens
    # done = True
    plant= input()
    while plant != ("bush" or "tree"):
        plant= input("There are two plants you can hide in. Type 'bush' to hide im the bush or 'tree' to hide in the tree")
        break
    if plant == "bush":
        print("A bunny from Alice in Wonderland finds you and takes you into her burrow. She has magical powers and offers to turn you into her species, or shrink you to her size. Type 'bunny' to turn into a bunny or 'shrink' to become her size.")
        magic= input()
        while magic != ("bunny" or "shrink"): 
            magic= input("Type 'bunny' to turn into a bunny or 'shrink' to become her size.")
        if magic == "bunny":
            print("You are adopted as the bunny\'s child and live happily ever after with the bunnies.")
        elif magic == "shrink":
            print("You become an ambassador for Burrow Basin, working with communications between Human World and Burrow Basin. You are loved by the bunnies.")
    elif plant == "tree": 
        print("Park Ranger Simon from Hell finds you in the tree. He kills you painlessly to take you to Hell. However, if you have more goodness than evil you can be saved. Type 'good' if you are mre good and 'evil' if you are more evil.")
        goodness= input()
        while goodness != ("good" or "evil") : 
            goodness= input("If you have more goodness than evil you can be saved. Type 'good' if you are more good and 'evil' if you are more evil.")
            break
        if goodness == "good":
            print("The angels feel your goodness and decide to rescue you from Simon.")
        elif goodness == "evil":
            print("The evil in you is pulled down by the gravitational pull in Hell. Simon likes the evil, so he lets you sleep in peace.")
    