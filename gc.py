import os

def gc(dna):
    gc_count = 0
    for i in dna:
        if (i == "G") or (i == "C"): # catch if i equals G or C
            gc_count += 1

    gc_content = (gc_count / len(dna)) * 100 # multiply by 100 to get percentage

    return gc_content

# read_FASTA function from lab 2
def read_FASTA(file_path):
    ''' Read FASTA file, output dict w/ all seqs keyed by name.
    
    Input: file path to FASTA file
    Output: dictionary with keys=sequence names (after
        > character) and values=corresponding
        amino acid or DNA sequence
    '''
    output_dict = {}
    # open file
    with open(file_path, "r") as f:
        seq = ""
        # convert file to list
        lines = f.readlines()
        for line in lines:
            if ">" in line: # check if > is in the current line
                key = line[1:].strip("\n ")
                if key not in output_dict:
                    output_dict[key] = []
            else:
                seq += line.strip("\n ")
                output_dict[key].append(line.strip("\n "))
        for key, seq in output_dict.items():
            # append each seq to its key
            output_dict[key] = "".join(seq)
    f.close()
    return output_dict

if __name__ == '__main__':
    # CHANGE CURRENT WORKING DIRECTORY TO THE DIRECTORY WHERE THIS FILE IS PLACED IN
    # IN THIS CASE, I WOULD HAVE IT IN MY lab-4 FOLDER

    programFilePath = os.getcwd()
    datasetFilePath = programFilePath + r"\datasets\rosalind_gc.txt"
    with open(datasetFilePath, "r") as f:
        
        output_dict = read_FASTA(datasetFilePath)

        max_gc_content_ID = ""
        max_gc_content = 0

        for key, seq in output_dict.items():
            if gc(seq) > max_gc_content: # changes max_gc_content and max_gc_content_ID when there is a new maximum
                max_gc_content_ID = key
                max_gc_content = gc(seq)

        print(max_gc_content_ID)
        print(max_gc_content)