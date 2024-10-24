from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    # Create instance of FastaParser
    fasta_parser = FastaParser('data/test.fa')
    # Create instance of FastqParser
    fastq_parser = FastqParser('data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print ("Transcribed RNA fa:")
    fasta_parser = FastaParser('data/test.fa')
    for header, sequence in fasta_parser:
        #print the parsed DNA from fasta to RNA sequence in a joint format
        print(transcribe(sequence))


       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print ("Transcribed RNA fq:")
    fastq_parser = FastqParser('data/test.fq')
    for header, sequence, quality in fastq_parser:
        #print the parsed DNA from fastq to RNA sequence in a joint format
        print (transcribe(sequence))


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print ("Reversed RNA fa:")
    fasta_parser = FastaParser('data/test.fa')
    for header, sequence in fasta_parser:
        #print the reversed RNA from the original fasta file
        print (reverse_transcribe(sequence))
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print ("Reversed RNA fq")
    fastq_parser = FastqParser('data/test.fq')
    for header, sequence, quality in fastq_parser:
        #print the reversed RNA from the original fastq file
        print (reverse_transcribe(sequence))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
