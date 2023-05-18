userName = input("enter your username : ")
password = input("enter your password : ")

if "admin" in userName and "admin" in password:
    print("welecome")
elif "admin" in userName:
    print("wrong data")
else:
    print(f"hello {userName}")
