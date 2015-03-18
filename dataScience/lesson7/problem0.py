# The goal is to create a function that removes punctuation from a string

sentence = raw_input('Enter a sentence please: ')
def unpunctuate(sentence):
# For each character in string
    for char in sentence:
# if it matches any of those in the string
        if char in "?.',!/;:":
# replace it with a space. sentence.replace takes (the character, the replacement)
            sentence = sentence.replace(char, '')
    print sentence

unpunctuate(sentence)
