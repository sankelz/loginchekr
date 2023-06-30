x = str(input("input a username!"))
def qualifications (x):
    if len(x) > 7:
        print ("great! now please select a password.")
        y = str(input("input a password!"))
        dict_login = {"username": "password"}
        dict_login["username"] = x
        dict_login["password"] = y
        return (dict_login)
    else:
        print ("please make sure your username has over 7 characters.")
print(qualifications(x))
