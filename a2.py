def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)    

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna1.count(dna2) >= 1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid.

    >>> is_valid_sequence('ATCGTCG')
    True
    >>> is_valid_sequence('ATBC')
    False
    """
    
    for char in dna:
        if char not in ('ACTG'):
            return False
    else:
        return True
 
        
def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 sequence into dna1 sequence at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATGCATTC', 'TGA', 4)
    'ATGCTGAATTC'
    """

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(n):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    """

    if n == 'A':
        return 'T'
    elif n == 'G':
        return 'C'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGA')
    'GCT'
    """

    sequence = ''
    for n in dna:
        sequence = sequence + get_complement(n)
    return sequence
