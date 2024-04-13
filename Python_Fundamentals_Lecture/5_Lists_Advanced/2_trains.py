def manage_train(train, command, *args):
    if command == "add":
        people = int(args[0])
        train[-1] += people
    elif command == "insert":
        index, people = int(args[0]), int(args[1])
        train[index] += people
    elif command == "leave":
        index, people = int(args[0]), int(args[1])
        train[index] -= people

num_wagons = int(input())
train = [0] * num_wagons

while True:
    user_input = input()

    if user_input == "End":
        break

    command, *args = user_input.split()
    manage_train(train, command, *args)

print(train)
