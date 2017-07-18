#!/bin/python

class Word():
  word = ""
  _type = ""

  def __init__(self, terms):
    self.word = terms[0]

  def __str__(self):
    return "(%s)%s" %(self._type, self.word)
  __repr__ = __str__
  
class Pronoun(Word):
  _type = "pronoun"
  def __init__(self, terms):
    self.word = terms[0]
    self.person = int(terms[2])

class Noun(Word):
  _type = "noun"
  plural = "{self.noun}s"

  def __init__(self, terms):
    self.word = terms[0]
    self.plural = terms[2]

class Article(Word):
  _type = "article"
    
class Verb(Word):
  _type = "verb"
  conjugaison = []
  
  def __init__(self, terms):
    self.word = terms[0]
    self.conjugaison = terms[3:]

wordTypes = {
  "word": Word,
  "pronoun": Pronoun,
  "noun": Noun,
  "verb": Verb,
  "article": Article
}

class MemoryParser():
  filename = ""
  memory = []

  def __init__(self, filename):
    self.filename = filename

  def parse(self):
    with open(self.filename) as f:
      for line in f.readlines():
        if not line.startswith("#") and len(line) > 1: #to avoid parsing commented lines and empty lines
          self.memory.append(self.build_word(line.replace('\n', '').split(';')))
    return self.memory

  def build_word(self, parsedLine):
    return wordTypes[parsedLine[1]](parsedLine)

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
