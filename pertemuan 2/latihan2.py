def is_password_valid(password):
    while True:
        if (
            len(password) == 8
            and any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)
        ):
            return True
