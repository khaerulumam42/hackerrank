def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        chars = string[i:(i+k)]
        remove_double = []
        for char in chars:
            if char not in remove_double:
                remove_double.append(char)
        print("".join(remove_double))
        
