import json

#User infomation

name = input("Name: ")
age = int(input("Age: "))

#Create Dictionary

user = {
    "name": name,
    "age": age,
}

#Save to JSON File
with open("user.json","w") as file:
    json.dump(user, file, indent=4)

#Load Save Date
with open("user.json","r") as file:
    saved_user = json.load(file)

#Displaying Saved Data
print("\nSaved User Data")
print(f"Name:{saved_user['name']}")
print(f"Age:{saved_user['age']}")

