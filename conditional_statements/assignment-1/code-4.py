# 4.wap to validate facebook username and password
# condition is:---> username-->"python"  and password="python masters"

username = input("username")
password = input("password")

if username == "python":
    if password == "python masters":
        print("Login Successful!!")
    else:
        print("invalid password")
else:
    print("invalid username")