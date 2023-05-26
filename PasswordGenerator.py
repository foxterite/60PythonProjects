# Import the random module to generate random elements
import random

# Prompt the user to enter the length of the password
passlen = int(input("Enter the length of the password: "))

# Define a string containing all the possible characters for the password
a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Generate a random password by sampling characters from the defined string without replacement
b = "".join(random.sample(a, passlen))

# Print the generated password
print(b)
