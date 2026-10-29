def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    """Find the most frequent k-mers (with mismatches and 
    reverse complements) in a DNA string.

    Given: A DNA string Text as well as integers k and d.

    Return: All k-mers Pattern maximizing the sum 
    Countd(Text, Pattern) + Countd(Text, Pattern) over all 
    possible k-mers."""
    
    def makePatterns(n: int) -> list[str]:
        patterns = []
        
        alphabet = "ACGT"
        for i in range(n):
            new_patterns = []
            
            # for all possible patterns...
            for pattern in patterns:
                # add all possible next letters
                for letter in alphabet:
                    new_patterns.append(pattern + letter)
            
            patterns = new_patterns

        return patterns

    def reverseComplement(pattern: str) -> str:
        rev = ""

        for letter in pattern:
            if letter == "A":
                rev = "T" + rev
            elif letter == "C":
                rev = "G" + rev
            elif letter == "G":
                rev = "C" + rev
            else:
                rev = "A" + rev

        return rev

    def hammingDistance(first: str, second: str) -> int:
        count = 0

        for i in range(len(first)):
            if first[i] != second[i]:
                count += 1

        return count
    
    
    
    # END HELPERS

    patterns = makePatterns(k) # to check all possible patterns of k
    counts = {}
    
    max = 0
    for pattern in patterns:
        reverse = reverseComplement(pattern)
        count = 0

        for i in range(len(text) - k +1):
            window = text[i:(i+k)]

            # check both the reverse and forward
            if hammingDistance(pattern, window) <= d:
                count += 1
            if hammingDistance(reverse, window) <= d:
                count += 1

        counts[pattern] = count
        
        if count >max:
            max = count

    # find the most frequents
    ret = set()
    for pattern in patterns:
        if counts[pattern] == max:
            ret.add(pattern)

    return ret
        
    
