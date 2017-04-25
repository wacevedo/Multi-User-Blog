import re

usernameRegex = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
passwordRegex = re.compile(r"^.{3,20}$")
emailRegex = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def valid_password(password):
    if password:
        return passwordRegex.match(password)


def verify_password(password, verifyPassword):
    return password == verifyPassword


def valid_username(username):
    if username:
        return usernameRegex.match(username)


def valid_email(email):
    if email:
        return emailRegex.match(email)
    else:
        return True
