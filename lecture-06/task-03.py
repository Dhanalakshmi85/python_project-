
airports = {}

while True:
    print("\nMenu:")
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit the program")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport added.")

    elif choice == "2":
        icao = input("Enter ICAO code to fetch: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

