def revp(dna_string):
    dna_bases_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reverse_complement = ""
    for base in dna_string:
        reverse_complement += dna_bases_dict[base]