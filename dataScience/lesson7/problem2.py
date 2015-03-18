__author__ = 'Me'
stringlist =  ("John likes to watch movies. Mary likes movies too." , " John also likes to watch football games.")
len(stringlist)

def unpunctuate(sentence):
    for char in sentence:
        if char in "_()?.',!/;:":
            sentence = sentence.replace(char, '')
    return sentence





def getbagofwords():
    myDic = {}
    for item in stringlist:
        unpunctuate(item)
        splititem =item.split()
        for word in splititem:
            if word in myDic:
                myDic[word] += 1
            else:
                myDic.update({word: 1})
    for keys,values in myDic.items():
        print(keys)
        print(values)


getbagofwords()
