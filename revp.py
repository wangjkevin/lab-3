import os

def revp(dnaString):
    dnaBasesDict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reverseComplement = ""
    for base in dnaString:
        reverseComplement += dnaBasesDict[base]
    reverseComplement = reverseComplement[::-1]
    
    for i in dnaString:
        for j in range(4, 13):
            pass
            

    print(reverseComplement)

if __name__ == "__main__":
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    arg = ""

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_revp.txt"
    with open(datasetFilePath, "r") as f:
        lines = f.readlines()

        arg = lines[1]
        print(revp(arg))
