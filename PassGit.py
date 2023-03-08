complete = False
user = {{"Franky" : "Apple"} , {"Abi" : "Poopyfart"}}

while not complete:
    username = input("What is your username? ")
    password = input("What is your password? ")
    conf_username = input("Repeat the username: ")
    conf_password = input("Repeat the password: ")

    if username != conf_username or password != conf_password:
        print("username or password does not match!")
        continue
    if not username in user:
        print("Input username again!")
    if password == user[username]:
        if [username] == user.find(username)
        print(f"User has been identified, Welcome {username}")
        complete = True
    else:
        print("Input password again")
