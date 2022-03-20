import os
f = open('me.txt')

full_name = f.readlines()[0]
print(full_name)
last_name = full_name[0:6]
first_name = full_name[6:18]
middle_name = full_name[18:27]

print(f" My first name:{first_name}\n My last name is: {last_name}\n My middle name is:{middle_name}")

print("\nThis is assignment bullet point 2: ")
print(f"   This is my local file path: {os.getcwd()}")


