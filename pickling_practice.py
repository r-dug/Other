import pickle


# Pickle module saves information to your disk. obviously this is very useful,
# so you can access that information later.


# Create something. In this case, a list, but it could be virtually anything.
fruit = ['banana', 'orange', 'cucumber', 'watermellon']

# print the list. this isn't necessary to save via pickle.
# it is only demonstrative in this exercise
print("List we are saving: \n", fruit)

# This line dumps the *information* to your disk from the python file.
# perhaps, a save function in a game could us input and an "if" statement
# to activate the pickle dump
pickle.dump(fruit, open('fruit.dat', 'wb'))

# now we will change the info in the *python* file, but not on the disk.
fruit.append("apple")

# print the newly amended list in python
print("List, as changed in the python file: \n", fruit)

# load the information from the pickle save earlier.
fruit = pickle.load(open('fruit.dat','rb'))

# now we print that list as it will now appear,
# i.e. as it is saved from the pickle dump.
print('List saved previously by pickle: \n', fruit)
