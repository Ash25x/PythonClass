print("Lets practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
#use \ to do nothing, use \t for tab and \n for new line
#print using all the \ options
poem = """
\tThe love world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend
\n\t\twhere there is none.
"""
#create a variable, use """ to type as much as you want
#use \t and \n
print("-----")
print(poem)
print("-----")
#print dashes then the variable then more dashes
#to make it look like poem
five = 10 - 2 + 3 - 6
#create a variable using addition
print(f"This should be five: {five}")
#print that variable in a sentence

#create  a functiom
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates
#use the argument in the function to do math for variables
#end in a return value for the variables
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#create a new variable and give it a value
#assign arguments to the function
print("With a starting point of: {}".format(start_point))
print(f"Wed have {beans} beans, {jars} jars, and {crates} crates.")
#print the sentences and use the argument and function in them
start_point = start_point / 10
formula = secret_formula(start_point)
print("We'd have {} beans {} jars, {} crates.".format(*formula))
#create a new variable and give it a value
#assign that variable to the function
#create a variable that holds the function
#print the arguments and function 
