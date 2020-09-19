def minion_game(string):
    vowels_char = "A,I,U,E,O".split(',')
    vowels = 0
    consonants = 0
    for i, char in enumerate(list(string)):
        if char in vowels_char:
            vowels += len(string)-i
        else:
            consonants += len(string)-i
    
    if vowels > consonants:
        print("Kevin {}".format(vowels))
    elif vowels < consonants:
        print("Stuart {}".format(consonants))
    else:
        print("Draw")
