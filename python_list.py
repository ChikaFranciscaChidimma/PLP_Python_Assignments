# 1. Create an empty list
my_list = []

# 2. Append the elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element from my_list
my_list.pop()

# 6. Sort my_list in ascending order
my_list.sort()

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Print the final list
print("Final my_list:", my_list)
