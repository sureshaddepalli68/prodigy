import re
import getpass

def assess_password_strength(password):
    # Criteria checks
    has_digit = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_special = any(char in r"!@#$%^&*(),.?\":{}|<>" for char in password)
    meets_length_requirement = len(password) >= 8

    # Count how many criteria are met
    criteria_met_count = sum([has_digit, has_uppercase, has_lowercase, has_special, meets_length_requirement])

    # Determine strength based on criteria met
    if criteria_met_count == 5:
        return "Password Strength Level: Very Strong (Meets all criteria)."
    elif criteria_met_count >= 3:
        return "Password Strength Level: Strong (Meets at least 3 criteria)."
    elif criteria_met_count == 2:
        return "Password Strength Level: Moderate (Meets at least 2 criteria)."
    else:
        return "Password Strength Level: Weak (Does not meet sufficient criteria)."

def main():
    print("---------------- Password Complexity Checking Tool -----------------")
    
    # Get password input securely
    password = getpass.getpass("Enter your password: ")

    # Mask the password for display
    masked_password = password[0] + '#' * (len(password) - 2) + password[-1]
    print("Entered Password: {}".format(masked_password))

    # Assess password strength
    result = assess_password_strength(password)
    print("")
    print(result)

    # Display password security tips
    print("\nHere are some tips for creating a secure password:")
    tips = [
        "1. Aim for at least 12 characters in length.",
        "2. Use a mix of uppercase, lowercase, numbers, and special characters.",
        "3. Avoid common words or easily guessable information.",
        "4. Do not use personal information like names or birthdays.",
        "5. Consider using passphrases or combining multiple unrelated words.",
        "6. Use unique passwords for each account.",
        "7. Change passwords periodically.",
        "8. Enable Two-Factor Authentication (2FA) where available.",
        "9. Be cautious of phishing attempts and suspicious websites.",
        "10. Use a password manager for secure storage of passwords."
    ]
    for tip in tips:
        print("- " + tip)

if __name__ == "__main__":
    main()