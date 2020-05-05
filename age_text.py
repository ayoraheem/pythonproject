age = ()
age = int(input( "Enter your age"))
if age < 2:
    print("person is a baby")
elif age < 4:
 print("person is todder")
#  dictonary
alen_0 = { "color": "green", "name": "Jhon", "point": 5}
print(alen_0["color"])

# key value in dic
user_0={ "usernmae":"Joh01", "first_name":"John", "last_name":'mark',"passsword":"lqw"}
print(print(user_0))
for key, value in user_0 .items():
    print(f"key: {key}")
    print(f"value:{value}")

student = {"stu_id": 1000, "first_name": "Mark", "last_name":"James", "dep": "compute_Eng", "date_birth":" 4-3-1979", "add": "1651 Timpson dr ,75126, texas"}
for key,value in student .items():
    print(f" key :{key}")
    print(f"value:{value}")

