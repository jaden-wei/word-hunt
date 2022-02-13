
with open('bigrams.txt') as file:
    bigrams = file.read().splitlines()

s = "ABCWX"
print(s[-2:] in bigrams)