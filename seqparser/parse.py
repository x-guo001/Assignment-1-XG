import io
from typing import Tuple, Union


class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        """
        Initialization to be shared by all inherited classes.
        
        # Recall that this is where we store baseline attribute of a class. For example:
            class Cat: 
                def __init__(self, weight: float, breed: str, food: str):
                    self.weight = weight
                    self.breed = breed
                    self.food = food
                    
        # What attributes are we initializing here in Parser? 
        """
        
        self.filename = filename

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Returns a sequencing record that will either be a tuple of two strings (header, sequence)
        or a tuple of three strings (header, sequence, quality). 

        """
        return self._get_record(f_obj)

    def __iter__(self):
        """
        This is an overriding of the Base Class Iterable function. Here, for the purposes of this
        assignment, we are defining how this class and all inherited classes interact with loops.

        # Usage

        ```
        parser_obj = Parser(filename)
        for record in parser_obj:
            # do something
        ```

        The code above calls `__iter__` and for every record it returns, does something with it.

        You may notice we use the keyword `yield` instead of `return` for this function. This is
        because our `__iter__` is what is known as a generator function, which generates an
        output then waits until it is called again to resume. In our case, it just reads in a
        record, outputs it, then waits to read the next record.

        In comparison, functions with `return` simply restart when they are called again, so we
        would just be reading from the beginning of the file.

        Generator functions are very useful for many bioinformatic tools where you don't need 
        everything loaded at once and instead are interested in interacting with the stream 
        (i.e. you need every value once and won't need it again after you use it). This saves
        quite a bit of memory, especially when you are working with billions of sequences and don't 
        need to keep all of them in memory. 
        
        """

        # The proper way to open a file for reading and writing in python3 is to use the `with` / `as` keywords.
        # and keep the I/O within the nested code block. This will save you from some really nasty bugs that
        # sometimes close a file before everything you expect to be written/read is written/read. 
        # 
        # the interpretation of the following code is that for the lifetime of the filebuffer 
        # returned by the `open` function it will be accessible as the variable `f_obj`, of type io.TextIOWrapper
        with open(self.filename, "r") as f_obj:
            
            # this loop will run forever or return an error, depending on your implementations of _get_record
            # but we will leave it up to you to implement the fix! 

            # hint: when reading a file, how do we know when to stop reading? what keyword should we use to stop a loop?

            while True:
                rec = self.get_record(f_obj)
                # TODO: stop the loop
                # stop the loop by adding 'break'
                if rec is None:
                    break
                yield rec

    def _get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
                """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`
                """)


class FastaParser(Parser):
    """
    Fasta Specific Parsing.
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str]:
        """
        TODO: returns the next fasta record as a 2-tuple of (header, sequence)
        """
        
        header = ""
        sequence = ""

        for line in f_obj:
            # remove white space from the line
            line = line.strip()
            # if the line start with >, it is a header line
            if line.startswith(">"):
                header = line    
            # if not a header, the line is sequence    
            else:
                sequence=line
            # if both header and sequence were found, return as (header, sequence)
            if header and sequence:
                return (header, sequence)
                 



class FastqParser(Parser):
    """
    Fastq Specific Parsing 
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]:
        """
        TODO: returns the next fastq record as a 3-tuple of (header, sequence, quality)
        """
        #remove the white space from header
        header = f_obj.readline().strip()
        if not header:
            return None
        #sequence file is followed by the header and remove any white space
        sequence = f_obj.readline().strip()
        #skip the third line followed by sequence line
        f_obj.readline()
        #quality file will be shown after the sequence line and the white space will be removed
        quality = f_obj.readline().strip()
        #fastq data will be displayed in the format of (header, sequence, quality)
        return (header, sequence, quality)


