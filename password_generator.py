import random
import string

def generate_password(length = 12):
    charactor = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(charactor) for _ in range(length))
    return password

print("Welcomme to the password generator!!")
length = int(input("Enter the length of the password: "))
print("Your password is : ",generate_password(length))