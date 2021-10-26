sum = 0
ptable = open("Periodic Table of Elements.csv", "r")
print(ptable.read())
while True:
    user_input = input("enter element and percent (X,%) or stop() to stop:")
    if user_input == "stop()":
        break
    else:
        user_input = user_input.split(",")
        sum += user_input[1]

