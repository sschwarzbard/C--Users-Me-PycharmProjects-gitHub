__author__ = 'Me'
wordlist = ["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
sentence = "The sun also rises, let's go to the movies"
def vectorize():
    sentence = "The sun also rises, let's go to the movies"
    wordlist = ["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
    bagofwords = sentence.split()
    myDic = {}
    for item in wordlist:
        if item in bagofwords:
            myDic.update({item: 1})
        else:
           myDic.update({item: 0})
    for keys,values in myDic.items():
        print(keys)
        print(values)
vectorize()