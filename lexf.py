import os
from itertools import product

def lexf(symbols, n): # in my case, symbols is the ordered list of the provided symbols in the dataset
    permutations = list(product(symbols, repeat=n))
    for item in permutations:
        print("".join(item))

if __name__ == '__main__':
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_lexf.txt"
    with open(datasetFilePath, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()] # get rid of \n
        symbols = [symbol for symbol in list(lines[0]) if symbol != " "] # get rid of extra spaces when converting to a list
        num = int(lines[-1])

        print(lexf(symbols, num))