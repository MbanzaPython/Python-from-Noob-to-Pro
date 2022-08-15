import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Have to add -1, since lists don't count from 0
random_pick = random.randint(0, len(names) - 1)
print(f"{names[random_pick]} is going to buy the meal today!")