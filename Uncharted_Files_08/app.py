sent_message = 'Hey there! This is a secret message.'

# Create the file and write the initial message
with open("C:\\Python course\\Intermediate python\\Uncharted_Files\\sent_message.txt", 'w') as file:
    file.write(sent_message)

# Open with 'r+' to read and then modify
with open("C:\\Python course\\Intermediate python\\Uncharted_Files\\sent_message.txt", 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()
    print(f"Original Message: {original_message}")

    # Move the cursor back to the beginning of the file
    file.seek(0)

    # Define the new message
    unsent_message = 'This message has been unsent.'

    # Write the new message over the old one
    file.write(unsent_message)

    # Truncate the file to the current cursor position
    # This removes any leftover characters from the original message
    file.truncate()

# Verify the change
with open("C:\\Python course\\Intermediate python\\Uncharted_Files\\sent_message.txt", 'r') as file:
    final_message = file.read()
    print(f"Final Message:    {final_message}")
