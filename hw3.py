from sys import argv

script, name, age = argv
Answers = 'Type your answer here --->'

print("Where do I start today?", script)
print(f"Have you finished {script} ?")
Answer1 = input(Answers)

print("If you did then great, lets get to know you a little better, if not get back to it before Saroosh gets mad")

print(f"What do your friends call you, what is your nickname {name}?")
nickn = input(Answers)


print(f"Wow so you are {age} years old, what is your favorite food?")
food = input(Answers)

print("What is your ideal vacation spot?")
vacay = input(Answers)

print("If you could have any power in the world, what would it be?")
power = input(Answers)

print(f"""
So I got to know you a bit better {name}, I got your age which is {age} years old.
Next I'll need your social. I'm kidding. I see your favorite food is {food}, lay low on those calories.
Your dream vacation is at {vacay}. And the power you desire the most is {power}.
Pretty interesting.

"""
)
