NLP Programming Exercises
We're going to work through these in class, some individually, some in groups and ultimately we'll review them together.

For those who are still new to Python, this will serve as practice
For those who are more confident in their Python, you, too, will learn some more advanced techniques and how to make your code more elegant and Pythonic.
Problem 0:

Write a function `unpunctuate` that takes a string and removes all punctuation, e.g.

unpunctuate("Hey there! How's it going?")
# will output the following
"Hey there Hows it going"
Problem 1:

Write a function `get_bag_of_words_for_single_document` that, given any string (also called document), e.g. "John also likes to watch football games.", returns its bag of words:

get_bag_of_words_for_single_document("John also likes to watch football games.")

# outputs the following. Hint: it doesn't have to be a dictionary exactly but could be an object that acts like a dictionary.
{
    'games.': 1,
    'to': 1,
    'football': 1,
    'watch': 1,
    'also': 1,
    'likes': 1,
    'John': 1
}
Problem 2:

Write a function `get_bag_of_words` that uses the above function to achieve the following: given a list of strings, it returns the total bag of words
for all of the documents.

get_bag_of_words([
    "John likes to watch movies. Mary likes movies too.",
    "John also likes to watch football games.",
])

# ouputs the following:
{
    'likes': 3,
    'watch': 2,
    'to': 2,
    'John': 2,
    'also': 1,
    'games.': 1,
    'movies': 1,
    'too.': 1,
    'movies.': 1,
    'football': 1,
    'Mary': 1
}
Problem 3:

Given a bag of words for all of the documents in our data set, write a function `turn_words_into_indices` take the keys in the bag of words and alphabetize them,

e.g.
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

turn_words_into_indices(bag_of_words_data)

# outputs the following:
["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
Problem 4:

Given a document, write a function `vectorize` that turns the document into a list (also will be called a vector) the same length as the number of keys of bag of words where
for each index of the list will be 1 only if the word at that index in the word list is contained in the document and 0 otherwise.

e.g.
Given this word list: ["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
Given this document: "The sun also rises"
vectorize("The sun also rises. Let's go to the movies")
# Since it contains 'also', 'to' and 'movies, the vectorize call will output the following
[1, 0, 0, 0, 0, 0, 1, 1, 0, 0]