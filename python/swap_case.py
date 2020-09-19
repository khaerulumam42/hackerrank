def swap_case(sentence:str) -> str:
    new_sentence = ""
    for char in sentence:
        if char.islower():
            new_sentence += char.upper()
        else:
            new_sentence += char.lower()
    return new_sentence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)