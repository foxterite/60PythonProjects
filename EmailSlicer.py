# Prompt the user to enter an email address and remove any leading or trailing whitespace
email = input("Enter Your Email: ").strip()

# Extract the username from the email address
username = email[:email.index('@')]

# Extract the domain name from the email address
domain_name = email[email.index("@")+1:]

# Create a formatted string that displays the extracted username and domain
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")

# Print the formatted string
print(format_)
