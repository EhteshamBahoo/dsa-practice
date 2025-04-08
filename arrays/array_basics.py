# Array is a linear data structure used to store multiples items of same type

# Disadvantage of array: fixed size (memory wastage), homogenous(lack of flexibility)




# Function to create an array
def create_array():
    arr = [1, 2, 3, 4, 5]
    return arr

# Function to append an element to an array
def append_to_array(arr, element):
    arr.append(element)
    return arr

# Function to remove an element from an array
def remove_from_array(arr, element):
    if element in arr:
        arr.remove(element)
    else:
        print(f"Element {element} not found in array.")
    return arr

# Function to find an element in an array
def find_in_array(arr, element):
    if element in arr:
        return f"Element {element} found at index {arr.index(element)}"
    else:
        return f"Element {element} not found in array."

# Function to iterate over an array
def iterate_array(arr):
    for elem in arr:
        print(elem)

# Function to reverse an array
def reverse_array(arr):
    return arr[::-1]

# Function to get the length of the array
def array_length(arr):
    return len(arr)

# Main function to demonstrate array operations
if __name__ == "__main__":
    arr = create_array()
    print("Created array:", arr)

    arr = append_to_array(arr, 6)
    print("Array after appending 6:", arr)

    arr = remove_from_array(arr, 3)
    print("Array after removing 3:", arr)

    print(find_in_array(arr, 4))
    print(find_in_array(arr, 10))

    print("Iterating over array:")
    iterate_array(arr)

    arr_reversed = reverse_array(arr)
    print("Reversed array:", arr_reversed)

    print("Length of the array:", array_length(arr))


#To solve homogenous issue we use refrential array

# Function to demonstrate referential behavior
def demonstrate_referential_arrays():
    # Create a list
    original_array = [1, 2, 3]
    print("Original array:", original_array)

    # Create another reference to the same list
    referential_array = original_array

    # Modify the referential array
    referential_array.append(4)
    print("After appending 4 to referential_array:")
    print("Original array:", original_array)  # Notice this changes too
    print("Referential array:", referential_array)

    # Modify an element in the referential array
    referential_array[0] = 100
    print("\nAfter modifying the first element in referential_array:")
    print("Original array:", original_array)  # The original array is also modified
    print("Referential array:", referential_array)

    # Now, let's create a new array with a copy of the original array (not a reference)
    copied_array = original_array.copy()
    copied_array.append(200)
    print("\nAfter copying original_array to copied_array and appending 200:")
    print("Original array:", original_array)  # No change to the original
    print("Copied array:", copied_array)  # The copied array is modified independently

# Main execution
if __name__ == "__main__":
    demonstrate_referential_arrays()