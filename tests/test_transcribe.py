# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """
    # pytest the positive transcribe test
    assert transcribe("ATCGGAT") == "UAGCCUA"
    # pytest the negative transcribe test
    assert transcribe("ATCGGAT") != "AAATT"

    pass


def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    # pytest the positive reverse transcribe
    assert reverse_transcribe("ATCGGAT") == "AUCCGAU"
    # pytest the negative reverse transcribe
    assert reverse_transcribe("ATCGGAT") != "AAATT"

    pass
