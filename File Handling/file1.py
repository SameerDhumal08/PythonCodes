# Creates file if it doesn't exist
file = open("sample.txt", "w")

file.write("Hello Sameer!\n")
file.write("Welcome to Python File Handling.")

file.close()

print("Data written successfully.")