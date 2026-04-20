def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        # Find the middle index
        middle = (left + right) // 2
        middle_element = search_list[middle]

        if middle_element == value:
            return middle
        
        # If the middle element is greater, eliminate the right half
        if middle_element > value:
            right = middle - 1
        # If the middle element is less, eliminate the left half
        else:
            left = middle + 1

    # If the loop finishes without returning, the value isn't there
    raise ValueError("value not in array")
