
names = set()

while True:
    name = input("Enter a name or press Enter to finish: ")

    if name == "":
        break

    # Check if name is new or existing 1
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nFinal Output:")
for name in names:
    print(name)
