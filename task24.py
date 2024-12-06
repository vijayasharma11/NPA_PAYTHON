# Function to read wages from a file and display them
def display_wages_file(file_name):
    # Open the file in read mode
    file = open(file_name, 'r')

    # Loop through each line in the file
    print("Employee Wages:")
    for line in file:
        # Split each line into name and wage
        name, wage = line.split()
        print(f"{name}: £{wage}")

    # Close the file after reading
    file.close()

# Specify the file name
file_name = 'wages.txt'

# Call the function to display wages
display_wages_file(file_name)