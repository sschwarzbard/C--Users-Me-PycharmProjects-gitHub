__author__ = 'Me'

sentence = raw_input('Enter a sentence please: ')
def unpunctuate(sentence):
    for char in sentence:
        if char in "?.',!/;:":
            sentence = sentence.replace(char, '')
    print sentence

unpunctuate(sentence)