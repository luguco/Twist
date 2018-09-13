import random


def shuffeler(word):
    # wort kann nicht getwistet werden
    if len(word) == 1 or len(word) == 2 or len(word) == 3:
        return word

    # Wort mit 4 Buchstaben könnte an 2. und 3. Stelle den gleichen Buchstaben haben -> 2. und 3. Pos. wird ohne
    # Überprüfung vertauscht
    if len(word) == 4:
        wrd = list(word)
        pos1 = wrd[1]
        wrd[1] = wrd[2]
        wrd[2] = pos1

        return ''.join(wrd)

    out = word
    # Wort muss getwistet sein
    while out == word:
        # Mitte wird gemischt
        mid = list(word[1:len(word) - 1])
        random.shuffle(mid)
        # Wort wird wieder zusammengesetzt
        out = word[0] + ''.join(mid) + word[len(word) - 1]
    return out


# Datei einlesen
file = open("files/twist5.txt", encoding='UTF-8').read()
charlist = list(file)
outlist = []

# Aufeinanderfolgende Buchstaben zu Wort zusammenfügen und shuffeln
latest_word = ''
for c in charlist:
    if c.isalpha():
        latest_word += c
    else:
        if latest_word != '':
            outlist.append(shuffeler(latest_word))
            latest_word = ''
        outlist.append(c)

print(''.join(charlist))
print('\n\n\n')
print(''.join(outlist))
