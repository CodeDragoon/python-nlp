#!/bin/python

from lexicon import *
from sys import argv
from nltk.tokenize import TweetTokenizer

class Processor():
  def __init__(self, lexicon):
    self.lexicon = lexicon

  def process(self, terms):
    found = []
    unknown = []
    for term in terms:
      word = self.lexicon.seek(term)
      if word:
        found.append(word)
      else:
        unknown.append(term)
    return found, unknown
  
def	main():
  string = argv[1]
  string = string[:1].lower() + string[1:]
  lexicon = LexiconParser("lexicon.csv").parse()
  processor = Processor(lexicon)
  tokenizer = TweetTokenizer()
  print(processor.process(tokenizer.tokenize(string)))
  return 0

if __name__ == '__main__':
  main()
