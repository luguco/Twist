def enttwister(word):
    # Wort kann nicht getwistet sein
    if len(word) < 4:
        return word
    # mögliche Wörter suchen
    char_ind = char_indice[word[0]]
    poswords_raw = wordlist[char_ind:]
    poswords = []
    for w in poswords_raw:
        if word[0] != w[0]:
            break
        if word[-1] == w[-1]:
            if len(word) == len(w):
                poswords.append(w)

    # Keine möglichen Wörter gefunden
    if (len(poswords)) == 0:
        return word

    # mögliche Wörter durchgehen und auf Richtigkeit überprüfen
    for e in poswords:
        el = list(e)
        fit = True

        for c in word:
            if c in el:
                el.remove(c)
            else:
                # Wort kann nicht passen
                fit = False
                break
        if fit and len(el) == 0:
            # Passendes Wort gefunden
            return e
    # Kein mögliches Wort hat gepasst
    return word


# Benötigte Dateien öffnen und Variablen nutzbar vorbereiten
wordlist_raw = open("files/woerterliste.txt", encoding='UTF-8').read()
file = open("files/enttwist.txt", encoding='UTF-8').read()

wordlist = wordlist_raw.splitlines()
wordlist.sort()

charlist = list(file)

char_indice = {}
lastletter = ''
i = 0

# Wörterliste durchgehen und Indizes der Anfangsbuchstaben finden -> Liste muss nicht jedes mal komplett durchgegangen
# werden
for word in wordlist:
    if word[0] != lastletter:
        lastletter = word[0]
        char_indice[word[0]] = i
    i += 1

outlist = []
latest_word = ''
# Aufeinanderfolgende Buchstaben zu Wort zusammenfügen und enttwisten
for c in charlist:
    if c.isalpha():
        latest_word += c
    else:
        if latest_word != '':
            outlist.append(enttwister(latest_word))
            latest_word = ''
        outlist.append(c)
print(''.join(outlist))
