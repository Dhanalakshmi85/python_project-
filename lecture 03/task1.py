


legal_size_limit = 42


zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length < legal_size_limit:
    short_by = legal_size_limit - zander_length
    print(f"The zander is too short! Release it back into the lake.")
    print(f"It is {short_by:.2f} centimeters short of the legal size limit.")
else:
    print("The zander is large enough to keep!")
