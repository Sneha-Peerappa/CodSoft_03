import random
import string

def generate_password(length, complexity):
    characters = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "special": string.punctuation
    }

    password = []
    if complexity == "low":
        char_set = characters["lowercase"] + characters["digits"]
    elif complexity == "medium":
        char_set = characters["lowercase"] + characters["uppercase"] + characters["digits"]
    else:
        char_set = characters["lowercase"] + characters["uppercase"] + characters["digits"] + characters["special"]

    for _ in range(length):
        password.append(random.choice(char_set))

    return "".join(password)


def main():
    print("Password Generator")
    length = int(input("Enter password length: "))
    print("Select complexity:")
    print("1. Low (lowercase letters and digits)")
    print("2. Medium (lowercase and uppercase letters, digits)")
    print("3. High (all characters, including special)")
    complexity_choice = input("Enter complexity choice (1/2/3): ")

    complexity = {
        "1": "low",
        "2": "medium",
        "3": "high"
    }.get(complexity_choice, "high")

    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()