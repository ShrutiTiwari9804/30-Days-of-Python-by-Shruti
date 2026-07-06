# ----------------------------------------------------------------------------
# Day 6 - Password Strength Analyzer
# 30 Days of Python Challenge
# -----------------------------------------------------------------------------


def check_length(password):
    return len(password) >=8

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any (char.islower() for char in password)

def has_number(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

    return any(char in special_characters for char in password)

def calculate_score(password):

    score = 0

    if check_length(password):
        score += 1 
    
    if has_uppercase(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    return score

def display_result(score):

    print("\nPassword Analysis")


    if score == 5:
        print("Strength : Very Strong")


    elif score == 4:
        print("Strength : Strong")


    elif score == 3:
        print("Strength : Medium")

    else:
        print("Strength : Weak")


def main():

    print("=" * 40)
    print("Password Strength Analyzer")
    print("=" * 40)

    password = input("Enter your password: ")

    score = calculate_score(password)

    display_result(score)

    print("\nChecklist")

    print(" ✔ Minimum 8 characters : ", check_length(password))
    print(" ✔ Uppercase letter : ", has_uppercase(password))
    print(" ✔ Lowercase letter : ", has_lowercase(password))
    print(" ✔ Number : ", has_number(password))
    print(" ✔ Special character : ", has_special_character(password))


if __name__ == "__main__":
    main()