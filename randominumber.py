#Importing random module to generate random numbers.
import random


#creating list
rand_list=[]
#Defining number of randoms to generate
n=10

#Looping 'n' times to generate random numbers, then appending to list
for i in range(n):
    rand_list.append(random.randint(2,2000))


#Printing list
print("Here is your list on numbers! ", rand_list)
