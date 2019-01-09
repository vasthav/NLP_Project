from train import training
import pickle

review_file = open('data.txt', 'r')
vocabulary_file = open('vocabulary.txt', 'r')
model_file = open('model', 'wb')

# reviews - Single review
# vocabulary - The complete vocabulary of words in the documents collections

reviews = review_file.read().splitlines()
vocabulary = vocabulary_file.read().splitlines()

"""
P1 - P(+) = total no of positive reviews / total no of reviews
P2 - P(-) = total no of negative reviews / total no of reviews
pp - Array of Positive liklihood of each word i.e. P(word | +) for each word
np - Array of Negative liklihood of each word i.e. P(word | -) for each word
"""

(P1, P2, pp, np) = training(reviews, vocabulary)
a = (P1, P2, vocabulary, pp, np)

# Dump the model into the file
pickle.dump(a, model_file)
model_file.close()
