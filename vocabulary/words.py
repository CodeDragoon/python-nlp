class Word():
  word = ""
  _type = ""

  def __init__(self, terms):
    self.word = terms[0]

  def __str__(self):
    return "(%s)%s" %(self._type, self.word)
  __repr__ = __str__
  
class InterrogativeWord(Word):
  _type = "interrogative"

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
  "article": Article,
  "interrogative": InterrogativeWord
}  
