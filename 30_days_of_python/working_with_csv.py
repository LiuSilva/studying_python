import csv

with open("data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Title', 'Description'])
	writer.writerow(['Row 1', 'Some desc'])
	writer.writerow(['Row 2', 'Some desc 2'])
	writer.writerow(['Row 3', 'Some desc 3'])

with open("data.csv", "a") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Title a', 'Description'])
	writer.writerow(['Row 1 a', 'Some desc'])
	writer.writerow(['Row 2 a', 'Some desc 2'])
	writer.writerow(['Row 3 a', 'Some desc 3'])

# each row is a list
with open("data.csv", "r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)

print()

# each row is a dictionary 
with open("data.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

with open("data.csv", "w") as csvfile:
	fieldnames = ['id', 'title']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'id': 123, 'title': 'title 1'})

print()
with open("data.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)	