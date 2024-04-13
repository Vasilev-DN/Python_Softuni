class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def print_party_info(self):
        print(f"Going: {', '.join(self.people)}")

        print(f"Total: {len(self.people)}")


party_instance = Party()

while True:
    name = input()

    if name == "End":
        break

    party_instance.add_person(name)

party_instance.print_party_info()
