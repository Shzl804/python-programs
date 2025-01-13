# Ask the user for a file name
file_name = input("Enter the name of the file (without extension): ")

# Add .txt extension if no extension is provided
if not file_name.endswith(".txt"):
    file_name += ".txt"

# Create and open the file in write mode
with open(file_name, "w") as file:
    file.write("This is a new file created with the name: " + file_name)

print(f"File '{file_name}' has been created successfully.")