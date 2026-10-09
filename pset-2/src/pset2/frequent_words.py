# from email.mime import text
# from frequent_words import FrequentWords as inclass_frequent_words
from pset2.pattern_count import patternCount

def frequentWords(text: str, k: int) -> set[str]:
    """consider adding docstring"""
    # 1. Handle edge cases to prevent max() errors on empty lists
    if not text or k > len(text) or k <= 0:
        return set()
        
    frequent_patterns = set()
    count = [0] * (len(text) - k + 1)
    
    # 2. Count occurrences using the in-class PatternCount function 
    # (Assuming it's available or called via the aliased module context)
    
    
    for i in range(0, len(text) - k + 1):
        pattern = text[i:(i+k)]
        count[i] = patternCount(text, pattern)
        
    max_count = max(count)
    
    # 3. Collect all patterns matching the maximum count
    for i in range(0, len(text) - k + 1):
        if count[i] == max_count:
            frequent_patterns.add(text[i:(i+k)])
            
    return frequent_patterns
