def temperature_converter():
    # Keep the running indefinetly untill condition is met
    while True:
        # Protecting user input error
        try:
            temp = float(input("Enter the temperature: "))
            print(temp)

        except ValueError:
            print("invalid value. please enter a number. ")
            continue
# asking the user for temperature
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()
# conditional statement
        if unit == "C":
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C is {fahrenheit}°F")

        elif unit == "F":
            celsius = (temp - 32) * 5/9
            print(f"{temp}°F is {celsius}°C")

        else:
            print("invalid unit. ")

        repeat = input("do you wan to continue? (yes/no). " ).lower()

        if repeat != "yes":
            print("thank you for using this app. goodbye")
            break

temperature_converter()