
gender = input("Enter your biological gender (female/male): ").strip().lower()


hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))


if gender == "female":
    normal_range_min = 117
    normal_range_max = 155
elif gender == "male":
    normal_range_min = 134
    normal_range_max = 167
else:
    print("Invalid gender input. Please enter 'female' or 'male'.")
    exit()


if hemoglobin_level < normal_range_min:
    print("Your hemoglobin level is low.")
elif normal_range_min <= hemoglobin_level <= normal_range_max:
    print("Your hemoglobin level is normal.")
else:
    print("Your hemoglobin level is high.")
