import re


def usernameValidity(usernama):
    if re.search('^[a-z][\w]{4,11}$', usernama):
        return True
    else:
        return False


def passwordValidity(password):
    if re.search('^(?=(?:\D*\d)\D*$)[A-Z0-9\W]{7}$', password):
        return True
    else:
        return False


print(usernameValidity("fiona_mareta"))
print(usernameValidity("fionamareta99"))
print(usernameValidity("FIONA_mareta"))
print(passwordValidity("1WORLD!"))
