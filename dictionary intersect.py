# This script opens two text files containing only words (four characters long) from http://www.gwicks.net/textlists/usa.zip and https://github.com/dwyl/english-words/blob/master/words_alpha.txt
# and creates a new file containing only the words that exist in both files.
# This script was created to help me find words that can be used in the NYTimes Spelling Bee.


# open the first file and read its contents into a set
with open('four.txt', 'r') as f:
  file1_words = set(f.read().split())

# open the second file and read its contents into a set
with open('words_alpha.txt', 'r') as f:
  file2_words = set(f.read().split())

# create a set of words that exist in both files
common_words = file1_words.intersection(file2_words)

# open the new file and write the common words to it
with open('robust.txt', 'w') as f:
  for word in common_words:
    f.write(word + '\n')
