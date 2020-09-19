def split_and_join(sentence: str) -> str:
    new_sentence = sentence.replace(" ", "-")
    return new_sentence
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)