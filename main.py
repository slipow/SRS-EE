import re


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

with open('SRS-EE/Culture.txt', 'r', encoding="utf-8") as file:

  for line in file:
    if not is_date(line):
      