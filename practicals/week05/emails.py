def main():
    email_from_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        verification = input(f"Is your name {name}? (Y/n) ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_from_name[email] = name
        email = input("Email: ")

    for email, name in email_from_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
