import random


def shuffeler(word):
    # wort kann nicht getwistet werden
    if len(word) <= 3:
        return word
    
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
    # Wort muss getwistet sein
    while out == word:
        mid = list(word[1:len(word) - 1])
        # Mitte wird gemischt
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
