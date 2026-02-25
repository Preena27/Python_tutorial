def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + key) % 26
            result += chr(start + new_pos)
        else:
            result += char
    return result
    
