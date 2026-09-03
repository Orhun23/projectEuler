import csv

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'C:\\Users\\OrhunErdogan\\OneDrive - Wefabricate\\Documents\\euler\\projectEuler-4\\largeSum\\input.csv'

# Initialize the total sum
total_sum = 0

# Open the CSV file and read the numbers
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        # Assuming each row contains a string of 50 digits separated by commas
        numbers = [int(digit_string) for digit_string in row[0].split(',')]
        total_sum += sum(numbers)

# Print the result
print(f"The sum of the numbers is: {total_sum}")
