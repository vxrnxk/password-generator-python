import string
import random


def generator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    pass_len = int(input('Enter the password length: '))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    pas = (''.join(s[0:pass_len]))

    print('Password generated:', pas)


generator()