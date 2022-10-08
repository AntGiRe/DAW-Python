def searchInWord(word, char):
  count = 0
  for i in word:
    if i == char:
      count += 1
  return count

print(searchInWord("hola hoy estas genial","h"));