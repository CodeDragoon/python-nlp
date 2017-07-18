#!/bin/python

from memory import *
from sys import argv

class Processor():
  def __init__(self, memory):
    self.memory = memory

  def process(self, string):
    found = []
    unknown = []
    terms = string.strip().split(' ')
    for term in terms:
      word = self.memory.seek(term.lower())
      if word:
        found.append(word)
      else:
        unknown.append(term)
    return found, unknown
  
def	main():
  string = argv[1]
  memory = MemoryParser("database.csv").parse()
  processor = Processor(memory)
  print(processor.process(string))
  return 0

if __name__ == '__main__':
  main()
