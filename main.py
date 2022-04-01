# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt", mode='r') as name_file:
    names = name_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()

for name in names:
    striped_name = name.strip()
    new_letter = contents.replace(PLACEHOLDER, striped_name)
    # print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode='w') as completed_letter:
        completed_letter.write(new_letter)
