class MyClass:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# Create instances of MyClass
item1 = MyClass("Name", "\033[91mJohn\033[0m")  # Set text color to red
item2 = MyClass("Age", "\033[92m30\033[0m")    # Set text color to green
item3 = MyClass("Country", "\033[94mUSA\033[0m")  # Set text color to blue

# Define the format for the table
table_format = "{:<15} {:<15}"

# Print the header
print(table_format.format("Key", "Value"))
print("-" * 30)

# Print the items in the table format
print(table_format.format(item1.key, item1.value))
print(table_format.format(item2.key, item2.value))
print(table_format.format(item3.key, item3.value))
