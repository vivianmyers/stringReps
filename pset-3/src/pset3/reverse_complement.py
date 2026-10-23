"""Rosalind BA1C: Find the Reverse Complement of a String."""


def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """
    ret = ""
    
    for char in text:
        if char == "A":
            ret += "T"
        elif char =="T":
            ret += "A"
        elif char == "C":
            ret += "G"
        elif char == "G":
            ret += "C"
    
    return ret[::-1]

print(reverseComplement("ATG"))