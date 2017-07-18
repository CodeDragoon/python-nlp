from vocabulary.words import *

class Memory():
  _memory_dict = {}
  _memory_array = []
  _memory_by_type = {}

  def __init__(self):
    return

  def append(self, word):
    self._memory_dict[word.word] = word
    self._memory_array.append(word)
    if word._type not in self._memory_by_type.keys():
      self._memory_by_type[word._type] = []
    self._memory_by_type[word._type].append(word)

  def seek(self, word):
    if word in self._memory_dict.keys():
      return self._memory_dict[word]
    for verb in self._memory_by_type['verb']:
      if word in verb.conjugaison:
        return verb
    

  def __str__(self):
    output = "["
    for index, word in enumerate(self._memory_array):
      output += "%s]" % word if (index == len(self._memory_array) - 1)  else "%s, " %word
    return output

class MemoryParser():
  filename = ""
  memory = Memory()

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
