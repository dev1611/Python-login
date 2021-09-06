
import task



print("press reg for registration , press login for authentication , press save to save to JSON ")
option = input("reg | login | save:")
if option == "reg":
    username = input("enter a username: ")
    password = input("enter the password: ")
    task.IdentityService.register(username,password)
elif option == "login":
    username = input("enter a username: ")
    password = input("enter the password: ")
    print(task.IdentityService.authenticate(username,password))
elif option == "save":
    path = input("enter the path with file name: ")
    task.IdentityService.save_to_json(path)