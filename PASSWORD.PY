import random
import string 
def generate_password(length):
    if length < 4:
        raise ValueError("Password must be at least 4 characters long")
    characters = string.ascii_letters + string.digits + "@_"
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice("@_"))
    for i in range(length - 4):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)
def main():
    length = int(input("Enter the desired length of the password (minimum 4): "))
    try:
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
