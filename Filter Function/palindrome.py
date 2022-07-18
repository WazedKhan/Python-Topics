def is_palindrome(value):
    return value[::-1].lower() == value.lower()


words = ("filter", "Ana", "hello", "world", "madam", "racecar")
print(list(filter(is_palindrome, words)))

