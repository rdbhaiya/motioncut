import random as r
import string

def generate_password(length, number, include_special=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all character types.")
    
    all_characters = string.ascii_letters + string.digits
    if include_special:
        all_characters += '!@#$%^&*_=+-'
    
    passwords = []
    for _ in range(number):
        password = [
            r.choice(string.ascii_uppercase),
            r.choice(string.ascii_lowercase),
            r.choice(string.digits)
        ]
        if include_special:
            password.append(r.choice('!@#$%^&*_=+-'))
        
        while len(password) < length:
            password.append(r.choice(all_characters))
        
        r.shuffle(password)
        passwords.append(''.join(password))
    
    return passwords

def main():
    try:
        print("\n======================================================\n")
        length = int(input("Enter the length of the password: "))
        number = int(input("Enter the number of passwords you want to generate: "))
        include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        passwords = generate_password(length, number, include_special)
        
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")
        print("\n======================================================\n")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
