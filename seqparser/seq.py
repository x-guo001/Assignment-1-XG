# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # make a DNA to RNA conversion dictionary 
    dna_to_rna = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    # transcribe the DNA sequence to RNA sequence following the converstion rule outlined above
    def rna_generator():
        for dna in seq:
            if dna in dna_to_rna:
                yield dna_to_rna[dna]
    return ''.join(rna_generator())
    


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    rna = transcribe(seq)
    #reversed the RNA sequence using 'reversed' function
    rna_reverse = ''.join(reversed(rna))
    return rna_reverse
