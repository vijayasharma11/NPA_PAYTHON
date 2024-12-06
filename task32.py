def read_hours():
    """Reads hours from the file and adds them to the hours list."""
    with open("hours.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.replace('.', '', 1).isdigit():  # Check if the value is numeric (allows one decimal point)
                hours.append(float(stripped_line))  # Store hours as float
            else:
                print(f"Invalid data in hours.txt: {stripped_line}")

def read_rate():
    """Reads rate from the file and adds them to the rate list."""
    with open("rate.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.replace('.', '', 1).isdigit():  # Check if the value is numeric (allows one decimal point)
                rate.append(float(stripped_line))  # Store rate as float
            else:
                print(f"Invalid data in rate.txt: {stripped_line}")

def read_name():
    """Reads names from the file and adds them to the name list."""
    with open("name.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            name.append(stripped_line)

def calc_wages():
    """Calculates and prints the wages based on hours and rate."""
    if len(name) != len(hours) or len(name) != len(rate):
        print("Error: The number of names, hours, and rates do not match.")
        return

    for i in range(len(name)):
        wage = rate[i] * hours[i]  # Calculate wage
        print(f"\n{name[i]}'s wages are £{wage:.2f}")

# Initialize lists to store file data
rate = []  
hours = [] 
name = [] 

# Main program
print("Reading from the files...\n")
read_hours()
read_rate()
read_name()

print("\nCalculating and displaying wages...\n")
calc_wages()
