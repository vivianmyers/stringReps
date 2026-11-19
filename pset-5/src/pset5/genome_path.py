def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    if not patterns:
        return ""

    genome = patterns[0]
    for kmer in patterns[1:]:
        genome += kmer[-1]

    return genome

# Example usage:
sample_path = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
print(stringSpelledByGenomePath(sample_path))  # Output: ACCGAAGCT
