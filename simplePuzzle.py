# Ash Ahmed and John Montes
#Naruto Ninja Game that tests you in scenarios to see if you can be a ninja
def naruto_affinity():
	print("\nSo you're training to be a ninja?")
	print("\nLet's see what your affinity is. Hold this paper")
	affinity = input("""\n-You hold the paper in your hand-\n
		\nInput 1 to burn the paper
		\nInput 2 to cut the paper
		\nInput 3 to crush the paper
		\nInput 4 to soak the paper
        \n >>""")
	if affinity == "1":
		print("\nLooks like your nature is fire")

	elif affinity == "2":
		print("\nLooks like your nature is wind")

	elif affinity == "3":
		print("\nLooks like your nature is earth")

	elif affinity == "4":
		print("\nLooks like your nature is water")

	else:
		print("\nLooks liike you haven't found an affinity yet. Keep trying")
		naruto_affinity()

naruto_affinity()

def death():
	print("\nYou died")
	answer = input("\nContinue?\n1 is yes\n2 is no\n>")
	if answer == "1":
		print("\nYou have a strong will!")

	elif answer == "2":
		print("\nYOU LOSE")
		return exit()
	else:
		return death()

def rogue():
    jutsu =input("""\nThere are 100 Rogue ninja attacking, which justu will you use?
    \nInput 1 chidori
    \nInput 2 Multi Shadow Clone Jutsu
    \nInput 3 Dragon Flame Jutsu
    \nInput 4 Run
    \n>>  """)
    if jutsu == "1":
        print("\nYou used chidori and killed 3 of them...then you died \n ")
        return death()

    elif jutsu == "2":
        print("\nYou used Multi Shadow Clone Jutsu and fought them off with your 100 clones ")

    elif jutsu == "3":
        print("\nYou used Dragon FLame Jutsu and burned them all to a crisp")

    elif jutsu == "4":
        print("\nYou died a cowards death! How did you plan on running from 100 ninjas? HUH?")
        return death()
    else:
        print("\nThe hell do you think you're doing you Bastard? Make a choice ")
        return death()
rogue()

def shuriken():
    trap = input("""\nYou stepped on a booby trap, a swarm of shuriken and kunais are launched at you,
what will you do?
\nInput 1 Substitution Jutsu
\nInput 2 Kamehamehaaa
\nInput 3 Block them with a sword
\nInput 4 It's an illusion
\n >>  """)
    if trap == "1":
        print("\nPoof! you substituted out, you're safe")

    elif trap =="2":
        print("\nYou wish you could do Kamehamehaaa, wrong anime idiot!")
        return death()
    elif trap == "3":
        print("\nThought you were cool huh, well you blocked 2 shuriken and the rest killed you")
        return death()
    elif trap == "4":
        print("\nHAH, you wish it was an illusion, you got impaled to death")
        return death()
    else:
        print("\nStop playing around, do you know how sharp Kunai's and shuriken are? ")
        return death()
shuriken()

def forest():
    snake =input("""\n You are in the forest of death and a massive 90 foot snake appears, what will you do?
\nInput 1 Throw kunais and shuriken
\nInput 2 Slice it up
\nInput 3 Summon Gamabunta
\nInput 4 Summon Gamakichi
\n >>  """)
    if snake == "1":
        print("\nWhat did you think that was going to do? It bounced off the snake and the snake ate you")
        return death()
    elif snake == "2":
        print("\nHAH Slice up a 90 foot snake, you're ego led to death")
        return death()
    elif snake == "3":
        print("\nYou summoned Gamabunta the 94 foot Toad with a sword, he sliced the serpents head off")

    elif snake == "4":
        print("\nYou summoned Gamabunta's son who is 2 feet tall, the snake ate you both")
        return death()
    else:
        print("\nYou're about to get eaten")
        return death()
forest()

def death_alt():
	print("\nCongratulations, you beat the game...")
	print("\nLegends never die")
	print("\nTO BE CONTINUED....We had more code and challenges but it had typos \nPlay our classes game for the deleted content!")
	return

death_alt()
