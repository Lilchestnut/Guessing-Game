print("""
Let's play a guessing game, I'll give you three options and only one is correct.
You score one point for every correct guess.
Are you ready?""")

answer = input()
if answer.lower() != "yes":
    print("Ok bye.")
    quit()


score = 0

# questions = {
    # "objects":["Grapes", "Mango", "Blueberry"]["Sneakers", "Boots", "Heels"]["Tiger", "Beaver", ""]
# }

print("""
a. Grapes  
b. Mango 
c. Blueberry"""
    )
answer = input()
if answer.lower() == "c":
    score += 1
    print("You are correct! \n")
else:
    print("Nope! Next one!")

print("""
a. Sneakers
b. Boots
c. Heels"""
    )
answer = input()
if answer.lower() == "b":
    score += 1
    print("You are correct! \n")
else:
    print("Nope! Next one!")

print("""
a. Tiger
b. Beaver
c. Penguin"""
    )
answer = input()
if answer.lower() == "b":
    score += 1
    print("You are correct! \n")
else:
    print("Nope! Next one!")

print("""
a. Guitar
b. Flute
c. Drum"""
    )
answer = input()
if answer.lower() == "a":
    score += 1
    print("You are correct! \n")
else:
    print("Nope! Next one!")

print("""
a. Lolipop
b. Popcorn
c. milkshake"""
    )
answer = input()
if answer.lower() == "c":
    score += 1
    print("You are correct! \n")
else:
    print("Nope! Next one!")

if score >= 3:
    print(f"""
You rock!!
Here is your score: {score}""")
else:
    print(f"""
Today's not your day.
Here is your score: {score}""")