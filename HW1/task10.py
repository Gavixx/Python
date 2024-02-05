# Create a dictionary of cadets with ks and their corresponding numbers
dict1 = {
    1: "Роман",
    2: "Дмитро",
    3: "Богдан",
    4: "Богдан",
    5: "Богдан",
    6: "Дмитро",
    7: "Алекс",
    8: "Іван"
}

# Create a dictionary of k-occurrence mapping
dict2 = {}

# Iterate through the cadet list and update the k-occurrence mapping
for i, k in dict1.items():
    if k not in dict2:
        dict2[k] = 1
    else:
        dict2[k] += 1

# Print the cadet list and k-occurrence mapping
print("Cadet list:")
print(dict1)
print("\nk-occurrence mapping:")
print(dict2)