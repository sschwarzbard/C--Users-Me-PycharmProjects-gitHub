__author__ = 'Me'
sentence = raw_input('Enter a sentence please: ')
def unpunctuate(sentence):
    for char in sentence:
        if char in "_()?.',!/;:":
            sentence = sentence.replace(char, '')
    return sentence
def get_bag_of_words_for_a_single_document(sentence):
    sentence = unpunctuate(sentence)
    bagofwords = sentence.split()
    milon = {}
    print bagofwords
get_bag_of_words_for_a_single_document(sentence)