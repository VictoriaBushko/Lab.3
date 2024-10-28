def is_isogram(string):
    lower_string = ''

    for char in string:
        if 'A' <= char <= 'Z':
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char
    seen_chars = []

    for char in lower_string:
        if char in seen_chars:
            return False
        seen_chars.append(char)

    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))