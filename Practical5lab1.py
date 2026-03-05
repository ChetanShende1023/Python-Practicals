# Tuple Program

t = tuple(map(int, input("Enter integers separated by space: ").split()))

# Total number of items
print("Total items:", len(t))

# Last item
print("Last item:", t[-1])

# Reverse tuple
print("Reverse tuple:", t[::-1])

# Check if 5 is present
if 5 in t:
    print("Yes")
else:
    print("No")

# Remove first and last items, sort remaining
new_tuple = list(t[1:-1])
new_tuple.sort()

print("Sorted remaining items:", tuple(new_tuple))