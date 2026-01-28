import csv
def create_text_file(filename, data):
    try:
        with open (filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"Error creating file: {e}")
def read_text_file(filename):
    try:
        with open (filename, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"Error reading file: {e}")
def append_text_file(filename, data):
    try:
        with open (filename, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"Error appending to file: {e}")
def create_csv_file(filename, rows):
    try:
        with open (filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        print(f"Error creating CSV file: {e}")
def read_csv_file(filename):
    try:
        with open (filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
# Example usage:
create_text_file('example.txt', 'Hello, World!\n')
append_text_file('example.txt', 'Appending some data.\n')
content = read_text_file('example.txt')
print("Text File Content:")
print(content)
create_csv_file('example.csv', [['Name', 'Age'], ['Alice', 30], ['Bob', 25]])
csv_data = read_csv_file('example.csv')
print("CSV File Content:")
for row in csv_data:
    print(row)
