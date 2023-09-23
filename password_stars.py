password_length = 10
while True:
    password = input("Password: ")
    if len(password) >= password_length:
        print(len(password) * '*')
        break
    else:
        print("Invalid password!")
