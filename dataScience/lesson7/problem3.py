__author__ = 'Me'
bag_of_words_data = {
    "John": 1,
    "likes": 2,
    "to": 3,
    "watch": 4,
    "movies": 5,
    "also": 6,
    "football": 7,
    "games": 8,
    "Mary": 9,
    "too": 10
}
mylist = []
def turn_words_into_indices():
    for word in bag_of_words_data:
        mylist.append(word)
    sortedlist = sorted(mylist, key=str.lower)
    print sortedlist

turn_words_into_indices()