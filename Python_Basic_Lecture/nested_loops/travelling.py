while True:
    destination = input("Enter the destination: ")

    if destination == "End":
        print("End")
        break

    min_budget = float(input("Enter the minimum budget for the trip: "))
    savings = 0.0

    while savings < min_budget:
        saving = input("Enter the amount saved (or 'exit' to end saving for this destination): ")

        if saving == "exit":
            break

        savings += float(saving)

    if savings >= min_budget:
        print(f"Going to {destination}!")
