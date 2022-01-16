def hamm(s, t):
    dH = 0 # hamming distance
    for i in range(len(s)):
        if s[i] != t[i]: # catch condition
            dH += 1
    return dH

print(hamm(
    "AGGAGTCAATTGTCGGCGTACCCTTCCGAACGACTTCTCTGTCTCCGTGAAATCCGGCTTTATGCGACCCAAATCTAAATTAGTTTTCACCCAGGGCGCCAGTACCCCGGTCCTAGCGATTCAGGAAATGCTAGCCCCGGACGACGAAACTAAGCATCTGCATGCCCATGATGGCCGGCCGTGGCTAATGGGATGACGTTACCTTCTGAACACCTATCTGAAGCCGATGCCAGGCGTCTGATACGTAACTCGAGACTTCTCACGACAAGCTACCGCCGGACATTGGACCCATTATCCGACGTGCCGTGTTCGATACATCGAGTAGCCTATAGCTGATCGGACTGCTTGCGTTAATAGCTCTCAGTCCTGGGTTGCATTGCCCTACCGAAGGCTATCGTCGTGCCTCTCTAATCCCGTGCGCATCTAACCTAGGTTCTGTGTCCGATTCTTAAGTGTGGGTCTTGAAAATCTTATATGAGTCACCTCAGATGCCCAGCTTCCCTTTCTGTATCGCGAAGTGCCGAAGTCTTCATGCCCTTGGGCGACTTCACTTAGTCCAGTGTAGTAATGCTTCTACCTGGCATTTGAAGGCAATAGGAATGGGCTATGGCAAGGATTCCGAGAGTCCGAAGGCAATGCTTACCTCGGTTGCGGCCGCTAATGGCGCGATAGTTGACACGATGGGTAATACTCGTAAAGATGTAACCTTCTCGAAGCATCTAGCACATCTGGGACAATGTCGCGCGACGTTTGTAATAGGTACAACCATTGTGCAGTGCGGTCATGCTTGCATGCCTCGGCGAGTTAGATATTCACAAATGCTCCACGTTGACACGAGTGGGTACGGGTGTAGGCTTAGCATCAATTGTGTTAACCGAGCCCATCCTATTGAACGGCTTCTGTTTTCGTTAATGCAGGAGACGGATGAGCACCACTAGTCGGGAAATCAATAGCAGGTGCTGCCTGCATCGGCGGGACA",
    "TCCGATCACTTGTACCCGAATCCCTACGAAGGCGTTGCCTGTTCCGGGGCGTCCCCCCCCCTAGTGCCACAGGGCTAAATTATTTGTCAGTAATCTAGCCTATGTCCCCACCCCCGCGATCGCGCAAACTCTCCCCTCACTGCACTTAATAAAGACCCCGAGTGACACTCATAGCTGGGCGTGCCTATTTGGACGCCCTTAAATATGCATAGCCCAGATGACTGGGACGTCTGACCTTTCCAAGTACAGTCGTGCAGACTCACGAAGTGTTACCGACGGAGGGGAGTCCCGTTATGGTATGTGGCATATTAGTGATCTCGAACAGGAAGAGCAGGTTCGCAATACTCAATGGCGGAGCCCGCAGATCTCGATTTAAAAGCCCTAGATCAGATGTTGAGCGCGCCTCTCTCAATCGGCGCCCATGGATCCTAGTTTGGATAGCGAATTAGTAAAATAGCCTGGGGAACAGTTACTTGCGGCCATAAAAGATGGCGCTAGAGCCTTCCTGCTCTCCGAAGCGTTGTCAATATCAGGCTCATTGGCGAGTTCCACTGCTTATGGGTAGTCGTGCCTCTGGCCTGCTCGTAACGTGGTTTCCTATGAGGTACAGCGAAGATTCCGCGACTCCGCCGGGAACGCGCACCTCGGAGTCCTCCCCTAACTACTCCATAGCCGAAACGCTCGTATTTAGCCTCTGGGCTGCTTCGGTCGCAAAAAGTCCTGGTATGTGCTGATACAAGTAGCTGGCGGATGTGATAGGTACAAGGATGGTTCAATTCCACCATGCCTATATGCTGCTGATACTTCGGTATACACAGAAGGTCCTAGGCGGCTTGAGTGGGGACTGGAATCTTGAATGCGTTATGTTAGCAGTGCGCTTCTATCCGGTCAATCGGTCAGGCTGCCGCTGACTTGCGTTCTCTGTTGAGGACTATGCCTAGGTAAATAAGTTACCGGCTGTGTCTGGCGGAAAGCGCCA"
))