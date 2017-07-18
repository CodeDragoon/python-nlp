from vocabulary.words import *

class Lexicon():
  _as_dict = {}
  _as_array = []
  _by_type = {}

  def __init__(self):
    return

  def append(self, word):
    self._as_dict[word.word] = word
    self._as_array.append(word)
    if word._type not in self._by_type.keys():
      self._by_type[word._type] = []
    self._by_type[word._type].append(word)

  def seek(self, word):
    if word in self._as_dict.keys():
      return self._as_dict[word]
    for verb in self._by_type['verb']:
      if word in verb.conjugaison:
        return verb
    

  def __str__(self):
    output = "["
    for index, word in enumerate(self._as_array):
      output += "%s]" % word if (index == len(self._as_array) - 1)  else "%s, " %word
    return output

class LexiconParser():
  filename = ""
  lexicon = Lexicon()

  def __init__(self, filename):
    self.filename = filename

  def parse(self):
    with open(self.filename) as f:
      for line in f.readlines():
        if not line.startswith("#") and len(line) > 1: #to avoid parsing commented lines and empty lines
          terms = line.replace('\n', '').split(';')
          if len(terms) > 1:
            self.lexicon.append(self.build_word(terms))
    return self.lexicon

  def build_word(self, terms):
    return wordTypes[terms[1]](terms)
