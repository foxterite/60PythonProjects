# Prompt the user to enter a phrase
user_input = str(input("Enter a Phrase: "))

# Split the input phrase into a list of words
text = user_input.split()

# Initialize an empty string
a = " "

# Iterate over each word in the list
for i in text:
    # Take the first character of each word, convert it to uppercase, and append it to the string 'a'
    a = a + str(i[0]).upper()

# Print the resulting string
print(a)
