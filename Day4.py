#Randomization and Python Lists

import random
import Day4_Module

random_number = random.randint(1,10)

print(random_number)


#Import Modules
print(Day4_Module.favorite_phrase)

#Example Exercise

random_coin = random.randint(0,1)

if random_coin == 0:
    print("Heads!")
else:
    print("Tails!")