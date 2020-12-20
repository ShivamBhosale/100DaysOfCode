import random
chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
len_of_pass=int(input("Enter the Length of the password: "))
def pass_gen(num):
    password=""
    for i in range(num):
        password += random.choice(chars)
    return password

print(pass_gen(len_of_pass))