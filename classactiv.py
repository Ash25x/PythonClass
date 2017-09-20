from sys import argv

script, file1, file2 = argv

file1op = open(file1)
whatsinside = file1op.read()

file2op = open(file2, 'w')
file2op.write(whatsinside)

#print(file2op)

file1op.close()
file2op.close()
