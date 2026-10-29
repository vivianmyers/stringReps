def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    def makePatterns(n: int) -> list[str]:
        patterns = [""]
        alphabet = ["A", "C", "G", "T"]

        for i in range(n):
            new_patterns = []
            for pattern in patterns:
                for letter in alphabet: 
                    new_patterns.append(pattern + letter)
            patterns = new_patterns

        return patterns

    def hammingDistance(a: str, b: str) -> int:
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count

    
    patterns = makePatterns(k)
    counts = {}
    max_count = 0

    for pattern in patterns: 
        count = 0
        for i in range(len(text) - k + 1):
            window = text[i:i+k]
            if hammingDistance(window, pattern) <= d:
                count += 1
        counts[pattern] = count
        if count > max_count:
            max_count = count

    
    result = set()
    for pattern in patterns: 
        if counts[pattern] == max_count:
            result.add(pattern)
            
    return result
