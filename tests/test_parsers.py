# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)
# import the tempfile to make the mock sequence in the test unit
import tempfile


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    # make a mock fasta sequence
    fasta_data = """>seq0
                    TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTC

                """
    # convert the mock fasta sequence to a temporary file for pytest
    temp_fasta = tempfile.NamedTemporaryFile(delete=False, mode='w+')
    temp_fasta.write(fasta_data)
    temp_fasta.close()
    #parser the temporary fasta file
    parser = FastaParser(temp_fasta.name)
    
    records = list(parser)
    #positive pytest for FastaParser from mock fasta file
    assert records[0] == (">seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTC")
    #negative pytest for FastaParser from mock fasta file
    assert records[0] != (">seq1", "GCCCGG")

    pass

    

def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    #make a mock fastq file for pytest
    fastq_data = """@seq0
                    TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCA
                    +
                    *540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>

                """
    #convert the mock fastq file into a temporary file for pytest
    temp_fastq = tempfile.NamedTemporaryFile(delete=False, mode='w+')
    temp_fastq.write(fastq_data)
    temp_fastq.close()

    parser = FastqParser(temp_fastq.name)
    records = list(parser)
    #positive pytest for FastqParser mock fastq file
    assert records[0] == ("@seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCA", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>")
    #negative pytest for FastqParser mock fastq file
    assert records[0] != (">seq1", "GCCCGG", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>")
    
    pass
