from auth import add_user,login_user
print(add_user("akshay1","1234"))
id=login_user("akshay1","1234")
print(id)
print(add_user("akshay1","123456"))
print(add_user("akshay1","123456"))