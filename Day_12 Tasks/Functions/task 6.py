def remove_last_key(**a):
    # Convert a keys to a list to find the last key
    keys = list(a.keys())
    
    if keys:  # Check if the dictionary is not empty
        last_key = keys[-1]  # Get the last key
        print("before removing list are:",a)
        d=a.pop(last_key)  # Remove the last key-value pair
        return a
    else:
        return {}  # Return empty dictionary if no keys

result = remove_last_key(a=10, b=20, c=30)
print("after removing list are:",result)


#method 2
def remove_last_key(**a):
    # Convert keys to a list to find the last key
    keys = list(a.keys())
    
    if keys:  # Check if dictionary is not empty
        last_key = keys[-1]  # Get the last key
        a.pop(last_key)  # Remove the last key-value pair
        return a
    else:
        return {}  # Return empty dictionary if no keys

# Step 1: Ask user how many key-value pairs
n = int(input("How many key-value pairs do you want to enter? "))

user_data = {}#creates an empty dictionary where we will add keys and values
# Step 2: Take input from user
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    user_data[key] = value

# Step 3: Call function with **user_data
result = remove_last_key(**user_data)

# Step 4: Show the result
print("Dictionary after removing the last key:", result)
