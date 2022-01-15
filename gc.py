import os

def gc(dna):
    gc_count = 0
    for i in dna:
        if (i == "G") or (i == "C"):
            gc_count += 1

    gc_content = (gc_count / len(dna)) * 100

    return gc_content

if __name__ == '__main__':
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    arg = ""

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_revp.txt"
    with open(datasetFilePath, "r") as f:
        lines = f.readlines()

        print(gc(arg))