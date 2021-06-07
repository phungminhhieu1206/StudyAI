print("--------- 0. String ---------")
print("Phung\nMinh Hieu")
print("Phung\"Minh Hieu")

# 1. String basic
print("--------- 1. String basic ---------")
phrase = "Hieu Dep Trai"
print("Show string in lowercase", end=': ')
print(phrase.lower())
print(phrase)
print(phrase.upper().isupper())
print("Length of string", end=': ')
print(len(phrase))

# 2. Index of string
print("--------- 2. Index of string ---------")
print("My string is", end=': ')
print(phrase)
print("The first char of string", end=': ')
print(phrase[0])
print("The last char of string", end=': ')
print(phrase[-1])

print("Index first found with character/substring ditermined", end=': ')
# print(phrase.index('i'))  # find 1 character
print(phrase.index('Dep'))  # find 1 substring

# 3. replace
print("--------- 3. Replace substring ---------")
print(phrase)
print(phrase.replace("Hieu", "Sang"))
