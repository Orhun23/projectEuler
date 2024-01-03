import csv

totalsum = 0

with open("C:\\Users\\OrhunErdogan\\OneDrive - Wefabricate\\Documents\\euler\\projectEuler-3\\largeSum\\input.csv", newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        row_number = int(''.join(row))
        totalsum += row_number

print(totalsum)

#todo: finish this fucker 