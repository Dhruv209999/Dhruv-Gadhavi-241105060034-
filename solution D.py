#print("Online Voting")

name = input("Enter name: ")
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

print("Voter:", name)

for i in range(3):
    print("Voted")

print("Exit")