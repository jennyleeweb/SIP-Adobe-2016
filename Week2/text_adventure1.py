start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maz;e.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and are surrounded by hungry sharks.") # finished the story by writing what happens
    done = True
    print("Luckily, there are two rocks you can jump over to escape. Type 'brown' to jump to the boulder or 'gray' to jump to the stone")
    rock= input()
    if rock == "brown":
        print("You escaped the sharks, and will need to hike up the mountain. You are stranded and need to get help. Type 'fire' to light a fire or 'stay' to live on the mountain forever.")
        help_signal= input()
        if help_signal == "fire":
            print("The President flies by in an airplane and sees your fire. He orders the pilot to land and rescues you out. Congratualtions!")
        else: 
            print("You find goats on the mountain and tame them. They become your loving pets and milk source and you live happily as a mountainman.")
    elif rock == "gray":
        print("You befriend the sharks and the sea gods order them to give you a ride home. Do not forget to get the phone number of the sharks!")
    while rock != "brown" or "gray":
        print("Luckily, there are two rocks you can jump over to escape. Type 'brown' to jump to the boulder or 'gray' to jump to the stone")
elif user_input == "right":
    print("You choose to go right and a scamming merchant follows you around. Luckily, there are two plants you can hide in. Type 'bush' to hide im the bush or 'tree' to hide in the tree") # finished the story writing what happens
    done = True
    plant= input()
    if plant == "bush":
        print("A bunny from Alice in Wonderland finds you and takes you into her burrow. She uses her magic to shrink you amd lets you join her family. The bunnies and you live happily ever after.")
    elif plant == "tree": 
        print("Park Ranger Simon from Hell finds you in the tree. He kills you painlessly to take you to Hell. However, if you have more goodness than evil you can be saved. Type 'good' if you are mre good and 'evil' if you are more evil.")
        goodness= input()
        if goodness == "good":
            print("The angels feel your goodness and decide to rescue you from Simon.")
        elif goodness == "evil":
            print("The evil in you is pulled down by the gravitational pull in Hell. Simon likes the evil, so he lets you sleep in peace.")
        while goodness != "good" or "evil" : 
            print("If you have more goodness than evil you can be saved. Type 'good' if you are more good and 'evil' if you are more evil.")
    while plant != "bush" or "tree":
        print("There are two plants you can hide in. Type 'bush' to hide im the bush or 'tree' to hide in the tree")
while user_input != "left" or "right": 
    print("Type 'left' to go left or 'right' to go right.")