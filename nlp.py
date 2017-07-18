#!/bin/python

from memory import *

class Tokenizer():
  raw = ""
  tokens = []
  
  def __init__(self, string):
    self.raw = string
    self.tokens = self.tokenize(string)

  def tokenize(self, string):
    words = string.split()
    return words

def	main():
  string = "I am a test"
  memory = MemoryParser("database.csv").parse()
  tokens = Tokenizer(string).tokens
  print(memory)
  print(tokens)
  return 0

if __name__ == '__main__':
  main()
