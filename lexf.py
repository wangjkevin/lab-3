import os

def lexf(symbols, n):
    pass

if __name__ == '__main__':
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_lexf.txt"
    with open(datasetFilePath, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]
        symbols = list(lines[0])
        # for symbol in symbols:
        #     if symbol == "":
        #         symbols.remove("")

        num = lines[-1]

        print(symbols)

        print(lexf(symbols, num))