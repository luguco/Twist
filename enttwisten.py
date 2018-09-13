def enttwister(word):
    if len(word) < 4:
        return word
    char_ind = char_indice[word[0]]
    poswords_raw = wordlist[char_ind:]
    poswords = []
    for w in poswords_raw:
        if word[0] != w[0]:
            break
        if word[-1] == w[-1]:
            if len(word) == len(w):
                poswords.append(w)

    if(len(poswords)) == 0:
        return word

    for e in poswords:
        el = list(e)
        fit = True
        for c in word:
            if c in el:
                el.remove(c)
            else:
                fit = False
                break
        if fit:
            return e
    return word


wordlist_raw = open("files/woerterliste.txt", encoding='UTF-8').read()
file = open("files/enttwist.txt", encoding='UTF-8').read()

wordlist = wordlist_raw.splitlines()
wordlist.sort()

charlist = list(file)


char_indice = {}
lastletter = ''
i = 0

for word in wordlist:
    if word[0] != lastletter:
        lastletter = word[0]
        char_indice[word[0]] = i
    i += 1

outlist = []
latest_word = ''
for c in charlist:
    if c.isalpha():
        latest_word += c
    else:
        if latest_word != '':
            outlist.append(enttwister(latest_word))
            latest_word = ''
        outlist.append(c)
print(''.join(outlist))
