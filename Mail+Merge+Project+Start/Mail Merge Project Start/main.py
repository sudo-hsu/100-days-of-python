#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

# Convert letter to a string
with open("./Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()

# Convert names to a list, removing any newlines
with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

for name in names_list:
    stripped_name = name.strip()
    new_letter = contents.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as letter_out:
        letter_out.write(f"{new_letter}")
