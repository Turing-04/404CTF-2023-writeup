# read input and return the letters in reverse order

print("Input file to which rules should be applied : ", end="")
original = input()

# rule 1
word = original[::-1]

# rule 2
# if number of letter is even then exchange first and the second part of the word
if len(word) % 2 == 0:
    mid = len(word) // 2
    word = word[mid:] + word[:mid]
else:
    # if number of letter is odd then fin the middle letter and remove it from the whole word
    middle = len(word) // 2
    word = word.replace(word[middle], "")

print(word)

# rule 3

# if the word as 3 letters or more:
# if the letter is a consonant, move the vowels to the left in the original word
# if the letter is a vowel, move the consonants to the right in the original word
     
# example : poteau => petauo // drapeau => drupaea


if len(word) >= 3:
    vowels = ""
    for l in original:
        if l in "aeiouy":
            vowels += l 
    print("voyelles : " + vowels)  
    
    rule3 = ""
    
    if word[2] in "aeiouy": # if vowel
        vowels = vowels[-1] + vowels[:-1] # move to the right
    else:
        vowels = vowels[1:] + vowels[0] # move to the left

    i=0
    for l in original:
        if l not in "aeiouy":
            rule3 += l
        else:
            rule3 += vowels[i] # move to the right
            i += 1

   
    word = rule3

    # then apply rule 1 and 2:
    word=word[::-1]
    
    if len(word) % 2 == 0:
        mid = len(word) // 2
        word = word[mid:] + word[:mid]
    else:
        # if number of letter is odd then find the middle letter and remove it from the whole word
        middle = len(word) // 2
        word = ''.join(word).replace(word[middle], "")

print(''.join(word))



# rule 4
# Pour `n` allant de 0 à la fin du mot, si le caractère `c` à la position `n` du mot est une consonne (majuscule ou minuscule), 
# insérer en position `n+1` le caractère de code ASCII `a = ((vp + s) % 95) + 32`, où `vp` est le code ASCII de la voyelle précédant 
# la consonne `c` dans l'alphabet (si `c = 'F'`, `vp = 'E'`), et `s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))`, 
# où `a{i}` est le code ASCII de la `i`-ième lettre du mot, `Id(x)` vaut `1` si `x` est vrai, `0` sinon, et `l{i}` la `i`-ième lettre du mot.

answer="" # soit j'ajoute la voyelle soit j'ajoute la coonsonne + son (ses) voisin(s)

word="futur"
for n in range(len(word)):
    if word[n] in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ": # if consonant

        # vp is the ASCII code of the vowel preceding the consonant c in the alphabet
        c = word[n]

        while c not in "aeiouyAEIOUY":
            print(ord(c), " = ", c)
            c = chr(ord(c) - 1)
        vp = ord(c)

        # s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))
        s = 0
        for i in range(n-1, -1, -1):
            s += ord(word[i]) * (2**(n-i)) * int(word[i] in "aeiouyAEIOUY")

        new_char = chr(((vp + s) % 95) + 32)
        
        answer += word[n] + new_char

    else:
        answer += word[n]

print(answer)