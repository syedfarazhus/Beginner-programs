from typing import TextIO

def freq(infile: TextIO, outfile: TextIO) -> None:
    """
    given a file containing one digit per line, writes to a file, 
    a column where numbers are the frequency of the digits
    """
    for line in infile:
        count = 0
        count += infile.count(int(line))
        outfile.write(line + str(count))
        
        
