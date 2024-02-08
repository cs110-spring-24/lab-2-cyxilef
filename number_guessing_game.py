import random
num = random.randint(1, 100)
user = 0
min = 1
max = 100
count = 0
while user != num:  # users number does not = #

    user = input(f"Enter your guess between {min} and {max}: ")
    user = int(user)

    if user > num:
        print("Too high")
        max = user
    elif user < num:
        print("Too low")
        min = user
    else:
        print("You got it!")

    count = count + 1
print(f'It took you {count} guesses to solve it! ')
# indentations matter
