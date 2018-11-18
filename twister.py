import random


# ----------------------------------------------------------------
# Fuktionen
# ----------------------------------------------------------------
def shuffeler(word):
    # Wort kann nicht getwistet werden, da es zu kurz ist
    if len(word) <= 3:
        return word

    # Wort kann nicht getwistet werden, da nur gleiche Zeichen in der Wortmitte vorhanden sind
    worker = list(word[1:len(word) - 1])
    last_c = worker[0]
    worker.pop(0)

    res = False
    for c in worker:
        if last_c != c:
            res = True
        last_c = c
    if not res:
        return word

    out = word
    # Wort muss getwistet sein (Bei z.B. symmetrischem Mittelteil notwendig)
    while out == word:
        mid = list(word[1:len(word) - 1])
        random.shuffle(mid)
        out = word[0] + ''.join(mid) + word[len(word) - 1]
    return out


# ----------------------------------------------------------------
# Hauptcode
# ----------------------------------------------------------------

# Datei einlesen
file = open("files/twist4.txt", encoding='UTF-8').read()
charlist = list(file)
outlist = []

# Aufeinanderfolgende Buchstaben werden zum Wort zusammengefügt und getwistet, Sonderzeichen werden geskippt
latest_word = ''
for c in charlist:
    if c.isalpha():
        latest_word += c
    else:
        if latest_word != '':
            outlist.append(shuffeler(latest_word))
            latest_word = ''
        outlist.append(c)

# Ausgabe: Ungetwistet  und getwistet
print(''.join(charlist))
print('\n\n\n')
print(''.join(outlist))
