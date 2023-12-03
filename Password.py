import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Secure Password Generator!")
    
    # Get user input for password length and quantity
    password_length = int(input("Enter the desired password length: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    
    # Generate passwords
    passwords = generate_multiple_passwords(num_passwords, password_length)
    
    # Display generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
