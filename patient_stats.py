def toFixed(value, digits):
    """Format a float to a fixed number of decimal places as a string."""
    return "%.*f" % (digits, value)

# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Patient Stats — List, Sort, and Average
# DATE WRITTEN: 12/14/2020
#
# PURPOSE: Create a list of patient names and their temperatures.
#          Display unsorted and bubble-sorted lists, then calculate
#          and display the average temperature. All output is written
#          to a user-specified external text file.
#
# VARIABLES (alphabetical):
#   avgTemperature  - calculated average of all patient temperatures
#   count           - loop control variable / index
#   elderPatient    - list of patient names (string)
#   fileName        - name of the output file
#   flag            - bubble sort flag; 0 = not sorted, 1 = sorted
#   outFile         - file object for writing output
#   size            - number of patient records to process
#   temp            - list of patient temperatures (float)
#   tempName        - temporary variable for swapping patient names
#   tempS           - temporary variable for swapping temperatures
#   totalTemp       - running total of all temperatures

# Define the output file name where the output will be written
fileName = input("Enter the file name where output will be written "
                 "(end with .txt) --> \n").strip()
outFile = open(fileName, "w")

# Validate and input the number of patient records to process
while True:
    try:
        print("How many patients' records will be processed? ")
        size = int(input())
    except ValueError:
        print("WRONG DATA TYPE ENTERED — please enter a positive whole number greater than zero.")
        print()
        continue
    else:
        if size <= 0:
            print("INVALID VALUE — please enter a positive whole number greater than zero.")
            continue
        else:
            break
    # end while True loop

# Declare lists in alphabetical order
# Patient name list (string)
elderPatient = [""] * size

# Patient temperature list (float)
temp = [0.0] * size

# Initialize processed variables
avgTemperature = 0.0
count = 0
totalTemp = 0.0

# WHILE LOOP to collect patient name and temperature data
while count < size:
    print("Enter the last and first name of patient #" + str(count + 1) +
          " [e.g. Williams, Robert]")
    elderPatient[count] = input().strip()

    # Validate temperature entry
    while True:
        print("Enter the temperature for " + elderPatient[count] + ": ")
        try:
            temp[count] = float(input())
            break
        except ValueError:
            print("Invalid input. Please enter a numeric temperature value.")

    # Update loop control variable
    count = count + 1
    # end while loop

# Reset the lcv for the next loop
count = 0

# Accumulate the total temperature
while count < size:
    totalTemp = totalTemp + temp[count]
    count = count + 1
    # end while loop

# Calculate the average temperature
avgTemperature = totalTemp / size

# Display and write the unsorted list heading
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 UNSORTED LIST ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("PATIENT NAME                 TEMPERATURE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
outFile.write("                 UNSORTED LIST \n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
outFile.write("PATIENT NAME                 TEMPERATURE\n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Reset lcv and display the unsorted patient list
count = 0
while count < size:
    line = elderPatient[count] + "                   " + toFixed(temp[count], 2)
    print(line)
    outFile.write(line + "\n")
    count = count + 1
    # end while loop

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

# BUBBLE SORT: sort patient list and corresponding temperatures by patient name
count = 0
flag = 0

# Outer loop continues as long as list is not fully sorted (flag == 0)
while flag == 0:

    # Assume the list is sorted until a swap is made
    flag = 1
    count = 0

    # Inner loop compares adjacent elements
    while count < size - 1:

        # If adjacent names are out of order, swap both name and temperature
        if elderPatient[count] > elderPatient[count + 1]:

            # Swap patient names
            tempName = elderPatient[count]
            elderPatient[count] = elderPatient[count + 1]
            elderPatient[count + 1] = tempName

            # Swap corresponding temperatures (must mirror name swap)
            tempS = temp[count]
            temp[count] = temp[count + 1]
            temp[count + 1] = tempS

            # A swap occurred — list is not fully sorted yet
            flag = 0
            # end if statement

        # Update inner loop control variable
        count = count + 1
        # end inner while loop
    # end outer while loop (bubble sort)

# Display and write the sorted list heading
print("             SORTED LIST BY NAME")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("PATIENT NAME                 TEMPERATURE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
outFile.write("             SORTED LIST BY NAME\n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
outFile.write("PATIENT NAME                 TEMPERATURE\n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Reset lcv and display the sorted patient list
count = 0
while count < size:
    line = elderPatient[count] + "                   " + toFixed(temp[count], 2)
    print(line)
    outFile.write(line + "\n")
    count = count + 1
    # end while loop

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

# Display and write the average temperature
avg_line = "AVERAGE TEMPERATURE = " + toFixed(avgTemperature, 2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(avg_line)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
outFile.write(avg_line + "\n")
outFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Close the external output file
outFile.close()
print("\nResults written to: " + fileName)

# END PROGRAM
