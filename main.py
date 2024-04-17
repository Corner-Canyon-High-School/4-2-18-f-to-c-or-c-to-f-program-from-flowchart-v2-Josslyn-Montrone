temp = int(input("Enter the the numerical temperature alone: "))
choice = input("Type 1 for Fahrenheight-to-Centigrade. Type 2 for Centigrade-to-Fahrenheight: ")
if choice == "1":
    converted_temp = (5/9) * (temp - 32)
    print("The converted temperature is " + str(converted_temp) + " Centigrade.")
elif choice == "2":
    converted_temp = (9 * temp + (32 * 5))/5
    print("The converted temperature is " + str(converted_temp) + " Fahrenheight.")
else:
    print("Invalid input.")
