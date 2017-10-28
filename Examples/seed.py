import random

random.seed( 10 )
print ("Random number with seed 10 : ", random.random())

# It will generate same random number
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())

# It will generate same random number
random.seed( 100 )
print ("Random number with seed 100 : ", random.random())