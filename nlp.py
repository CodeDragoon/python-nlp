#!/bin/python

from lexicon import *
from sys import argv

class Processor():
  def __init__(self, lexicon):
    self.lexicon = lexicon

  def process(self, string):
    found = []
    unknown = []
    terms = string.strip().split(' ')
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
  print(processor.process(string))
  return 0

if __name__ == '__main__':
  main()
