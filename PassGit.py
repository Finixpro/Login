complete = False
user = ["Franky" , "Apple" , "Abi" , "Poopyfart"]

while not complete:
    username = input("What is your username? ")
    password = input("What is your password? ")
    conf_username = input("Repeat the username: ")
    conf_password = input("Repeat the password: ")
    
    if username != conf_username or password != conf_password:
        print("username or password does not match!")
        
    if not username in user:
        print("Input username again!")
        
    if user.index(password) != -1:
        print(f"User has been identified, Welcome {username}")
    else:
        print("Input password again")
