from cgi import print_form
import re
from datetime import datetime
from time import sleep


def is_date(line):

  # if dont find "/"...
  if line.find("/") == -1:
    return False

  line_length = len(line)

  if line_length != 11 and line_length != 9:
    return False

  first_char = int(line[0])
  sev_char = int(line[6])

  basic = first_char < 4 and sev_char == 2

  if not basic:
    return False

  # 01/32/2020
  if line[3] == 3 and line[4] > 2:
    return False

  if line[0] == 1 and line[1] > 2:
    return False

  contains_letters = re.search('[a-zA-Z]', line)

  if contains_letters:
    return False
  
  return True




def DaysCounter(line):
  metaphysicPeacesDate = datetime.strptime(line.strip(), '%m/%d/%Y')

  now = datetime.now()

  interval = now - metaphysicPeacesDate
  days = interval.days

  # print(metaphysicPeacesDate)
  # print(now)
  # print(interval)
  # print(interval.days())
  
  return days



def BreakLists():
  # 1°  3 days 
  # 2°  7 days after the 1°
  # 3°  14 days after the 2°
  # 4°  1 month after the 3°
  # 5°  2 months after the 4°
  # 6°  4 months after the 5°
  # 7°  7 months after the 6°
  # 8°  10 months after the 7°
  # 9°  1 year after the 8°
  # 10° 1.5 years after the 9°
  # 11° 2 years after the 10°
  # 12° 2 years after the 11°
  # 13° 2 years after the 12°
  # and so on...

  month = 30
  year = 365

  firstBreak= 3
  secondBreak= 7
  thirdBreak = 14
  fourthBreak = month
  fifthBreak = month * 2
  sixthBreak = month * 4
  seventhBreak = month * 7
  eighthBreak = month * 10
  ninthBreak = year
  tenthBreak = year + 182
  eleventhBreak = year * 2

  breaksList = [int(firstBreak), int(secondBreak), int(thirdBreak), int(fourthBreak), int(fifthBreak), int(sixthBreak), int(seventhBreak), int(eighthBreak), int(ninthBreak), int(tenthBreak), int(eleventhBreak)]

  return breaksList


def practice(line, word):
  word_str = ''.join(word)
  spaced_line = line.replace(word_str, "    ")
  phrase_dllink = dllink_generator(line)
  print(f'Really try catch the word by listenyng: {phrase_dllink}')
  print()
  print(spaced_line)
  input("When ready, press enter.")

  print()
  print(line)
  input("When you've understood, press enter.")

  print()
  word_dllink = dllink_generator(word_str)
  print(f"Understand the word better: {word_str}")
  print(word_dllink)
  print()
  input("When term, press enter.")

  print()
  print("Re-write the assertion: ")
  assertion = sentence_part(line, word_str)
  print(assertion)
  rewrite = input()
  print(f'Re-write: {rewrite}')
  print()
  input("When you've understood, press enter.")

  print()
  print("Next case:")
  print()
  sleep(0.7)


def dllink_generator(line):

  words_split = line.split()
  deepL_link = "https://www.deepl.com/translator#en/pt/"

  for word in words_split:
    deepL_link += word
    if word != words_split[len(words_split)-1]:
      deepL_link += '%20'

  return deepL_link

def can_cut(words_split, index, direction):
  last_index = len(words_split) - 1
  if direction == 'r':
    if (last_index - index) < 2:
      return False
    return True
  if direction == 'l':
    if (index - 2) == 0:
      return False
    return True

def sentence_part(line, word):
  words_split = line.split()
  term_line = len(words_split)
  for index, split_word in enumerate(words_split):
    if split_word == word:
      if can_cut(words_split, index, 'r'):
        line = ""
        for i in range (index+2, len(words_split)-1):
          if len(words_split[i]) > 3:
            for j in range(0, i):
              line += words_split[j]
              if j != i:
                line += " "
            term_line = i
            break
      break
  for index, split_word in enumerate(words_split):
    if split_word == word:
      if can_cut(words_split, index, 'l'):
        line = ""
        for i in range (index-2, 0, -1):
          if len(words_split[i]) > 3:
            for j in range(i, term_line):
              line += words_split[j]
              if j != term_line:
                line += " "
            break
      break
  return line

  
with open('Culture.txt', 'r', encoding="utf-8") as file:

  letsPractice = False
  words_to_learn = []

  for line in file:

    # ignore "comments"
    if line.find('#') != -1:
      continue
    # if the line is empty or contains only whitespaces...
    if not line or str.isspace(line):
      continue

    if is_date(line):
      print(line)
      days = DaysCounter(line)
      print(days)
      snowball = 0
      breaks = BreakLists()

      # check if its time to practice the words of the day of that line
      for b in breaks:
        snowball += b
        if days == snowball:
          letsPractice = True
          # show the words date
          print(line)
          break
        else:
          letsPractice = False
      continue

      # is_date block finished

    # if the line isn't a 'comment' nor a 
    # date nor a word, so the line is a 
    # phrase and may it will be practiced
    if letsPractice:
      # if the line isn't a 'comment' or a 
      # date, so the line is a word or a phrase
      words_line = line.split()
      qtt_words = len(words_line)
      # if is a words, its added to practice
      if qtt_words == 1:
        words_to_learn.append(words_line)
        continue
      for word in words_to_learn :
        practice(line, word)
    # Here, or the practice finished or the
    # phrase will not be practice; In both 
    # cases the words_to_learn should be emmptied
    words_to_learn.clear()
    #print()

    # than, the next line will be processed

    # for line block finished

  # file finished