"""
This piece of code allows an user to compare strings of DNA to find matches
between codons that have been set in the 'sample-list'.
"""

sample = ['GTA', 'GGG', 'CAC']
print # for tab
def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data


def dna_codons(dna):
    codons = []
    for i in range(0, len(dna), 3):
        if (i + 3) < len(dna):
            codons.append(dna[i:i + 3])
    return codons


def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
    return matches


def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)

    if num_matches >= 3:
        print "File used: %s" % dna_sample
        print "Number of codon matches: %d" % num_matches
        print "The investigation should continue.\n"
    else:
        print "File used: %s" % dna_sample
        print "Number of codon matches: %d" % num_matches
        print "Amount of matches is not signficant."
        print "Suspect should be set free.\n"


is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
