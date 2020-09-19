# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    num_words = int(input())
    words = []
    for _ in range(num_words):
        word = input()
        words.append(word)

    set_words = {}
    for word in words:
        if word not in set_words.keys():
            set_words[word] = 1
        else:
            set_words[word] += 1
    print(len(set_words.keys()))
    for occurence in set_words.values():
        print(occurence, end=" ")
