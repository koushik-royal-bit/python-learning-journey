# Day 006 - DSA Arrays
# Beginner-friendly solutions for basic array problems


def find_maximum_element(arr):
    """Return the largest value in the array."""
    if not arr:
        return None

    maximum = arr[0]
    for num in arr[1:]:
        if num > maximum:
            maximum = num
    return maximum


def find_minimum_element(arr):
    """Return the smallest value in the array."""
    if not arr:
        return None

    minimum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
    return minimum


def sum_of_array_elements(arr):
    """Return the total sum of all values in the array."""
    total = 0
    for num in arr:
        total += num
    return total


def count_even_and_odd_numbers(arr):
    """Count even and odd numbers in the array."""
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


def reverse_array_two_pointers(arr):
    """Reverse an array using the two-pointer technique."""
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Example usage
numbers = [12, 45, 7, 23, 89, 34]

print("Original array:", numbers)
print("1. Maximum element:", find_maximum_element(numbers))
print("2. Minimum element:", find_minimum_element(numbers))
print("3. Sum of array elements:", sum_of_array_elements(numbers))
print("4. Even and odd counts:", count_even_and_odd_numbers(numbers))
print("5. Reversed array:", reverse_array_two_pointers(numbers.copy()))
