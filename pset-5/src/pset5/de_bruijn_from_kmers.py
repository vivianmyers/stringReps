from collections import defaultdict

def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    edges = []

    for kmer in patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        edges.append([prefix, suffix])

    return edges

# Example:
sample_patterns = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
print(deBruijnFromKmers(sample_patterns))
