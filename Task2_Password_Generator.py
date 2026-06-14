import random
import string

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Get password length from the user
length = int(input("Enter the desired password length: "))

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nGenerated Password:", password)
