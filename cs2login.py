name = input("Username: ")
password = input("Password: ")
if name == "alice" and password == "greenfingers":
    print("Welcome back", name)
    
elif name == "bob" and password == "builder":
    print("Welcome back", name)
        
elif name == "carol" and password == "danvers":
    print("Welcome back", name)
        
else:
    print("Wrong username or password")