
def rogue():
    jutsu =input("There are 100 Rogue ninja attacking, which justu will you use?  \nInput 1 chidori \nInput 2 Multi Shadow Clone Jutsu \nInput 3 Dragon Flame Jutsu \nInput 4 Run >>  ")
    if jutsu == "1":
        print("You used chidori and killed 3 of them...then you died \n ")
        return

    elif jutsu == "2":
        print("You used Multi Shadow Clone Jutsu and fought them off with your 100 clones ")

    elif jutsu == "3":
        print("You used Dragon FLame Jutsu and burned them all to a crisp")

    elif jutsu == "4":
        print("You died a cowards death! How did you plan on running from 100 ninjas? HUH?")

    else:
        print("The hell do you think you're doing you Bastard? Make a choice ")

rogue()

def shuriken():
    trap = input("""You stepped on a booby trap, a swarm of shuriken and kunais are launched at you,
     what will you do? \nInput 1 Substitution Jutsu \nInput 2 Kamehamehaaa \nInput 3 Block them with a sword \nInput 4 It's an illusion""")
    if trap == "1":
        print("Poof! you substituted out, you're safe")

    elif trap =="2":
        print("You wish you could do Kamehamehaaa, wrong anime idiot!")

    elif trap == "3":
        print("Thought you were cool huh, well you blocked 2 shuriken and the rest killed you")

    elif trap == "4":
        print("HAH, you wish it was an illusion, you got impaled to death")

    else:
        print("Stop playing around, do you know how sharp Kunai's and shuriken are? ")
shuriken()

def forest():
    snake =input("""You are in the forest of death and a massive 90 foot snake appears, what will you do?
    \nInput 1 Throw kunais and shuriken \nInput 2 Slice it up \nInput 3 Summon Gamabunta \nInput 4 Summon Gamakichi""")
    if snake == "1":
        print("What did you think that was going to do? It bounced off the snake and the snake ate you")

    elif snake == "2":
        print("HAH Slice up a 90 foot snake, you're ego led to death")

    elif snake == "3":
        print("You summoned Gamabunta the 94 foot Toad with a sword, he sliced the serpents head off")

    elif snake == "4":
        print("You summoned Gamabunta's son who is 2 feet tall, the snake ate you both")

    else:
        print("You're about to get eaten")

forest()
