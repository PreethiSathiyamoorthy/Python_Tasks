words=["madam","Apple","racecar","level","python"]
print(words)
for word in words:
    print(word,"is palindrome:"if word == word[::-1]else "is not a palindrome")
