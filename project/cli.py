def register_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
   
    user = {
        "email": email,
        "password": password,
        "name": name
    }
    database = []

    database.append(user)
    print("Registration successful!\n")

def login_user():
    global isLogin
    email = input("Enter your email to login: ")
    password = input("Enter your password to login: ")
   
    for user in database:
        database = {}
        if user['email'] == email and user['password'] == password:
            isLogin = True
            print("Login successful! Welcome, {}.\n".format(user['name']))
            return
   
    print("Login failed! Incorrect email or password.\n")
    
def show_database():
    database = []
    if isLogin:
        print("Current Database Records:")
        for user in database: 
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print("You need to be logged in to view the database.\n")
    
def main():
    while True:
        print("Welcome to the CLI")
        print("1. Register")
        print("2. Login")
        print("3. Show Database")
        print("4. Exit")
       
        choice = input("Enter your choice: ")
       
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            show_database()
        elif choice == '4':
            print("Exit the program.!")
            break
        else:
            print("Invalid choice. Please try again.\n")


    main()
