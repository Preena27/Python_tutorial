def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) != 10:
        return False
    digits = clean_isbn[:-1]
    check_char = clean_isbn[-1]
    if not digits.isdigit():
        return False
    val_list = [int(d) for d in digits]
    
    if check_char == 'X':
        val_list.append(10)
    elif check_char.isdigit():
        val_list.append(int(check_char))
    else:
        return False 
    total_sum = 0
    for i in range(10):
        total_sum += val_list[i] * (10 - i)
    return total_sum % 11 == 0
