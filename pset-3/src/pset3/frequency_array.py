"""Rosalind BA1K: Generate the Frequency Array of a String."""
def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    # TODO: Implement the frequency array.
    raise NotImplementedError("Implement frequencyArray for Rosalind BA1K.")
from collections import Counter
from itertools import product

def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    #Generate all 4^k possible k-mers in order
    alphabet = ["A", "C", "G", "T"]
    all_kmers = ["".join(p) for p in product(alphabet, repeat=k)]

    #Count occurrences of all k-mers present in text
    counts = Counter(text[i : i + k] for i in range(len(text) - k + 1))

    #Construct the frequency array in order and return it
    frequency_array = [counts[kmer] for kmer in all_kmers]
    return frequency_array


Text = "CGCAGAAACGCTACAGCTATTGTAATACGTCATGCTAGTCGCTGATGGACGAGCTAAGCGTTACATTCTCTCTTAGGCTCCTCGGAATTCCAGTTCATATCTGGTTAAAAGCGGTTCAGGTTCGAAGTTAACCACTCGCCCGCGTGGACGTCAAATGCAAAGTGCCTTTTCCCTCTAGATCCGCATTTTGGAAACGGTAATCAACATATATAGGTTCGCCCCTTTTTGCTCCCCAGGCCATGGGCTGTACTTTTAACAGCAAGCTAATCCCTTCACTATACTCGGCCAGACATAACAAAAGCTGGTTGGGAGGTCACGTGAATTCGACGCGGGCGACAGTTATCTAAAGTGTTTTACGAAAAGTTGGAATGTCGAACCACCCAAATTTCCTATTTTAAAACTGATTTAGGTGTTGGGGGCTTATCACTACTTACGGCGCCGCATACCTACCACGATAGTCACTCAGCTCAACCTAGAGTGTGCGTCGAAAGAGCCTAGAGGCCGTTATGAACACGCGCACTTGCTAGATGGATGCATGAGAAAGAACGTTCACTCTTTAGTCAATCGCATCCGTACGTCACCTTACACGCATTCGTCTACCACTATATAACACATGGATAAAGCTCCCAAAGCCAAGCAGGTGTCCTGGTTAGT"
K = 6

result = frequencyArray(Text, K)
print(result)
