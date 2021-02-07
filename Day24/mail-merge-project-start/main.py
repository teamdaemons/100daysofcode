# TODO: Create a letter using starting_letter.txt
with open("input/Names/invited_names.txt", "r") as file:
    # with open("./input/Names/invited_names.txt", "r") as file: //relative path
    invited_names = file.readlines()
    print(invited_names)
with open("input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()
for name in invited_names:
    name_final = name.strip("\n")
    x = starting_letter.replace("[name]", name_final)
    with open(f"./Output/ReadyToSend/letter_for_{name_final}.txt", mode="w") as final_letter:
        final_letter.write(x)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
