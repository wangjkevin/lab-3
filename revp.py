import os

def revp(dnaString):
    dnaBasesDict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reverseComplement = ""
    for base in dnaString:
        reverseComplement += dnaBasesDict[base]
    
    output = [] # list of tuples -- (position, length)

    for i in range(len(dnaString)):
        for j in range(4, 13):
            if (i + j) > (len(dnaString)): # catch if the index goes out of range
                break

            if dnaString[i:(i + j)] == reverseComplement[i:(i + j)][::-1]: # reverse reverseCompliment since we are looking for palindromes
                output.append((i + 1, len(dnaString[i:(i + j)])))

    for k in output:
        print(" ".join(map(str, k)))

if __name__ == "__main__":
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    arg = ""

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_revp.txt"
    with open(datasetFilePath, "r") as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line.strip("\n"))

        arg = "".join(new_lines[1:]) # starting on index 1 to ignore ID name

        print(revp(arg))