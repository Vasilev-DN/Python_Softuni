def sort_todo_notes(todo_notes):
    sorted_notes = []

    for note in todo_notes:
        importance, text = note.split('-', 1)
        importance = int(importance)

        inserted = False
        for i in range(len(sorted_notes)):
            if importance < sorted_notes[i][0]:
                sorted_notes.insert(i, (importance, text))
                inserted = True
                break

        if not inserted:
            sorted_notes.append((importance, text))

    return [text for importance, text in sorted_notes]



todo_list = []
while True:
    note = input()
    if note == "End":
        break
    todo_list.append(note)

sorted_todo_list = sort_todo_notes(todo_list)

print()
print(sorted_todo_list)
