import secrets
import string


def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    def is_pw_strong(pwd):
        return (
                any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2
        )

    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))
        if is_pw_strong(pwd):
            return pwd


if __name__ == '__main__':
    print(create_pw())
