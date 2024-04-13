def is_palindrome(word):
    return word == word[::-1]

words = input().split()
palindrome = input()

found_palindromes = [word for word in words if is_palindrome(word)]

print(found_palindromes)

palindrome_count = found_palindromes.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
