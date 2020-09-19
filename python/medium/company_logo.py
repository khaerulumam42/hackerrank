# UNSOLVED

import math
import os
import random
import re
import sys

def count_top_three(company: str):
    to_list = list(company.replace(" ", ""))
    set_of_char = set(to_list)

    chars = []
    count_char = []
    for char in set_of_char:
        chars.append(char)
        count_char.append(to_list.count(char))
    
    top_3_count = sorted(count_char[-3:])
    top_3_char = {}
    for numb in top_3_count:
        for i, count in enumerate(count_char):
            if count == numb:
                top_3_char[chars[i]] = count

    return top_3_char

if __name__ == '__main__':
    s = input()

    results = count_top_three(s)
    print(results)
