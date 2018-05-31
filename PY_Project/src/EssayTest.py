from nltk import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain
import csv


with open('train.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=False, delimiter=',')
    data = list(readCSV)
    vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in data]))
    
    #print(vocabulary)
    feature_set = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary}, tag) for sentence, tag in data]
    #print(feature_set)

    classifier = nbc.train(feature_set)

    with open('train.txt') as f:
        lines = f.read().splitlines()
    test_sentence = lines.__str__()
    print(test_sentence)
    featurized_test_sentence = {i: (i in word_tokenize(test_sentence.lower())) for i in vocabulary}

    print("Test Essay :", test_sentence.__str__())
    print("Essay Status : ", classifier.classify(featurized_test_sentence))