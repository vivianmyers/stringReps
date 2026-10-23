"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""


def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.
    """
    clumps = set()
    
    for i in range(len(genome) - L + 1):
        window = genome[i:i + L]
    
        counts = {}
        #count kmers within the window
        for j in range(len(window) - k + 1):
            pattern = window[j:j + k]

            if pattern in counts:
                counts[pattern] += 1
            else:
                counts[pattern] = 1

        # at least t times
        for pattern in counts:
            if counts[pattern] >= t:
                clumps.add(pattern)

    return clumps
    
    
