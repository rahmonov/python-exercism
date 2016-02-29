from string import maketrans

trantab = maketrans('GCTA', 'CGAU')


def to_rna(dna):
    return dna.translate(trantab)
