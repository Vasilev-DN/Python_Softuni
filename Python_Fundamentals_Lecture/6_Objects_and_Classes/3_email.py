class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    input_data = input().split()

    if input_data[0] == "Stop":
        break

    email = Email(input_data[0], input_data[1], ' '.join(input_data[2:]))
    emails.append(email)

indices_to_send = list(map(int, input().split(', ')))

for index in indices_to_send:
    if 0 <= index < len(emails):
        emails[index].send()

for email in emails:
    print(email.get_info())
