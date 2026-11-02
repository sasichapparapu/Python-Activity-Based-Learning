password = input("Enter a password: ")
errors = []

if len(password) < 8:
    errors.append("Must be at least 8 characters")

if not any(char.isupper() for char in password):
    errors.append("Needs an uppercase letter")

if not any(char.islower() for char in password):
    errors.append("Needs a lowercase letter")

if not any(char.isdigit() for char in password):
    errors.append("Needs a number")

if "password" in password.lower():
    errors.append("Cannot contain 'password'")

if any(password[i] == password[i + 1] == password[i + 2]
       for i in range(len(password) - 2)):
    errors.append("Cannot repeat a character three times")

if errors:
    for error in errors:
        print(error)
else:
    print("Password is valid")