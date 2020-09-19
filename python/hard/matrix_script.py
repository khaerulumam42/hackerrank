# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import string
# import re
# punct = string.punctuation

# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])

# matrix = []

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

# string = "".join(matrix)
# results = str()
# last_idx = 0
# for i in range(m):
#     for j in range(n):
#         results += string[last_idx-(i*n*m-i)]
#         last_idx += 3
# # translator = string.maketrans(punct, ' '*len(punct))
# # results = results.translate(translator).strip()
# # results = results.strip(punct)
# # results = re.sub(' +', ' ', results)
# print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', results))

#!/bin/python3

import re

# Import original script
matrix = list()
for _ in range(int(input().split()[0])):
    matrix.append(list(input()))

# Rotate the matrix
matrix = list(zip(*matrix))

# Prep regex sample
sample = str()
for subset in matrix:
    for letter in subset:
        sample += letter
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))
    