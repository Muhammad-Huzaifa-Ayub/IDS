
# Scenario 9: Text Message Analyzer

message = input("Enter a sentence or message: ")

print("\nOriginal Message:", message)
print("Total Characters:", len(message))
print("Length Without Leading and Trailing Spaces:", len(message.strip()))

vowels = 0
digits = 0
spaces = 0

for ch in message:
    if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
        vowels = vowels + 1

    if ch >= '0' and ch <= '9':
        digits = digits + 1

    if ch == ' ':
        spaces = spaces + 1

print("Number of Vowels:", vowels)
print("Number of Digits:", digits)
print("Number of Spaces:", spaces)

search_text = input("Enter a word or phrase to search for: ")

if search_text.lower() in message.lower():
    print("Search Result: Word or phrase found.")
else:
    print("Search Result: Word or phrase not found.")

print("Uppercase Message:", message.upper())
print("Lowercase Message:", message.lower())


