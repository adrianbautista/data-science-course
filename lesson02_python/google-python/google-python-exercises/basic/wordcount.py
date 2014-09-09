#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re
import code

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
class WordCounter(object):
  def __init__(self, filename):
    self.filename = filename
    self.word_text = ''
    self.words = []
    self.word_dict = {}

  def print_words(self):
    self.check_for_word_count_tuple()
    for word_count in self.word_count_tuple:
      print "{word_count[0]}: {word_count[1]}".format(word_count=word_count)

  def print_top(self):
    self.check_for_word_count_tuple()
    for word_count in self.word_count_tuple[0::21]:
      print "{word_count[0]}: {word_count[1]}".format(word_count=word_count)

  def check_for_word_count_tuple(self):
    try:
      self.word_count_tuple
    except AttributeError:
      self.generate_word_count_tuple()

  def generate_word_count_tuple(self):
    self.read_file()
    self.split_file()
    self.count_words()
    self.order_words()

  def read_file(self):
    self.word_text = open(self.filename, 'r').read()

  def split_file(self):
    self.words = self.word_text.split()

  def count_words(self):
    for word in self.words:
      sanitized_word = self.sanitize_word(word)
      self.check_for_word(sanitized_word)

  def sanitize_word(self, word):
    return re.sub('[^a-zA-Z0-9]', '', word).lower()

  def check_for_word(self, word):
    if word in self.word_dict:
      self.word_dict[word] += 1
    elif len(word):
      self.word_dict[word] = 1

  def order_words(self):
    self.word_count_tuple = sorted(self.word_dict.items(), key=lambda x: x[1], reverse=True)

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  word_counter = WordCounter(filename)

  if option == '--count':
    word_counter.print_words()
  elif option == '--topcount':
    word_counter.print_top()
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
