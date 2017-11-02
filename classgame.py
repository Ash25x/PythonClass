class Leaf:

        def mission1(self):
            print("""\nHey you're back.This will be way tougher, you die, you start over
Three years have passed since we last left off.
You were training outside the village and now you've come home
Upon arrival, there you notice a group of villagers that have red eyes
staggering around. They are villagers you know and stagger towards you
        """)

            action =input("""What will you do?
                \n Input 1 Greet them and try to help
                \n Input 2 Stab them
                \n Input 3 Use the Lightning Blade
                \n Input 4 Use your Sharingan
                \n >>> """)

            if action == '1':
                print("""\nWho the hell goes up to staggering people with red eyes?
They have been cursed with a exploding technique. They grab
onto you and explode. """)
                exit()
            elif action == '2':
                print("""\nNot friendly are ya? You stabbed one and your sword
got stuck. The rest surrounded you and exploded...they were
cursed with an exlosive jutsu""")
                exit()
            elif action == '3':
                print("""\nOh fancy huh? You sliced through 2 of them. But the
lightning blade is an up close technique, you got too close
and the rest exploded""")
                exit()
            elif action == '4':
                print("""\nYou used the Sharingan, an eye technique, simply by making
eye contact, you were able to put the villagers to sleep and
snap them out of that cursed exploding jutsu""")
                return


        def mission2(self):
            print("""\nSo you dealt with the exploding zombies.
As you walk outside the village borders. You see a massive 90 foot
tall Gorilla Titan. It spots you and starts scooping up big rocks/boulders and
heaving them at you.""")

            action1 =input("""\n What will you do?
            \n1 Use the Kamehamehaaa and blow the hairy bastard away!
            \n2 Use the Spirit Bomb
            \n3 Make a clone to distract it, while you sneak up on it's back
            \n4 Run
            \n >>>   """)

            if action1 == '1':
                print("""\nUgh you're annoying. Did you not learn from the
last game? You know what? Fine I'l let you use it this time
You blew the Gorilla titans legs off and it toppled over""")

            elif action1 == '2':
                print("""\nIdiot! This is not DragonBall Z! and even
if it was that move takes forever. Titan grabbed you ate you""")
                exit()

            elif action1 == '3':
                print("""\nYou were able to climb onto the back of it's neck
after a huge long trip and slash it, killing the Titan""")

            elif action1 == '4':
                print("""\nThis thing is 90 feet tall. You tried running
and it caught up and stomped your ass out""")

            else:
                print("A titan is about to kill you idiot, do something")

        def mission3(self):
            print("""\nYou notice there is a puddle and a scarecrow
ahead of you on a sunny as you are about to cross a long bridge.
You are in a rush to go complete a mission and get that good ninja paycheck """)

            action2 =input("""\n How will you proceed?
            \n1 Run towards the bridge
            \n2 Make a shadow clone to go to the bridge
            \n3 Throw a explosive kunai at the scarecrow
            \n4 Stomp on the puddle
            \n >>>   """)

            if action2 == '1':
                print("""\nYou ran towards he bridge, as you were crossing
the Demon brothers appeared and cut the bridge. You fell to your death""")
                exit()

            elif action2 == '2':
                print("""\nGood eye! Why is there a puddle on a sunny day in a place where it hasn't rained in days. Your shadow clone went out to cross the bridge.
\nThe Demon brothers rose up from inside the puddle and attacked the clone thinking it was you. You were able to sneak up on both and use Lightning blade to pierce
a hole through both their chests""")


            elif action2 == '3':
                print("""\nThe scarecrow exploded. You feel its safe now to
cross the bridge.As you head towards it, you get impaled by a giant claw""")
                exit()
            elif action2 == '4':
                print("""\nWhat are you 9? Stomping puddles? The Demon brothers
were in there and got angered and ripped you to shreds""")
                exit()
            else:
                print("Get your shit together and proceed!!!")
                exit()
class Sand:
    def mission4(self):
        print("""So you made it this far. You're wandering through a desert. You take a
step and a bunch of mines start going off! """)

        action3 =input("""\n What will you do?
        \n1 Make shadow clones of yourself
        \n2 Burrow yourself underground
        \n3 Jump high into the air
        \n4 Stab your sword into the floor and use lightning on it
        \n >>>   """)
        if action3 == '1':
            print("""\nYou made shadow clones of yourself and triggered
more mines...dead""")
            exit()
        elif action3 == '2':
            print("""\nThere were mines hidden underground as you burrowed,
you got blasted sky high like Team Rocket""")
            exit()
        elif action3 == '3':
            print("""\nDid you forget about gravity? You have to launched
and then BOOM DEAD""")
            exit()
        elif action3 == '4':
            print("""\nIn this world, lightning nullifies mines. You channeled
lightning into your sword and disabled the mines around you. Safe to continue
towards the Sand village""")

        else:
            print("Get your shit together and proceed!!!")
            exit()

    def mission5(self):
        print("""\nYou made it to the Sand village. You are greeted with a feast and welcomed.
After the feast you rest. In the middle of the night, you hear screaming and explosions going off.
It's the S Rank Ninja Diedara attacking the village. He is flying around and dropping explosives.
He drops a giant explosive towards the villagers.""")

        action4 =input("""\n What will you do?
        \n1 Guard them with a Sand Barrier
        \n2 Blast it with Fireball Jutsu
        \n3 Kamehamehaaa
        \n4 Blast the explosive with lightning
        \n >>>   """)
        if action4 == '1':
            print("""\nYou protected the villagers!! They will remember this""")

        elif action4 == '2':
            print("""\nFire and explosives don't mix. You made the explosion
bigger and got everyone killed""")
            exit()
        elif action4 == '3':
            print("""\nYa...I'm not letting you get away with that again.
Wrong anime fool!!""")
            exit()
        elif action4 == '4':
            print("""\nYou neutralized the explosive, but the explosive still came
down and crushed villagers.""")
            exit()
        else:
            print("Get your shit together and proceed!!!")
            exit()






class Bonus():
    def Link(self):
        c = input("""You see a rift in time and see a boy dressed in green
		          The boy stays Silent but draws his sword. What do you do?
				  \nInput 1 for Try and reason
				  Input 2 for Prepare to fight""")
        if c == '1':
            print("You were able to dodge thanks to the reflexes your visual prowess grant you!")
            return AB
        elif c == '2':
            print("Your swords clash and sparks fly")
            return exit()

x = Leaf()
x.mission1()
x.mission2()
x.mission3()
x = Sand()
x.mission4()
x.mission5()
#xy.mission6()
y = Bonus()
y.Link()
