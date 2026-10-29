def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    """Given: Strings Pattern and Text along with an integer d.

    Return: All starting positions where Pattern appears as 
    a substring of Text with at most d mismatches."""
    
    ret = list()
    
    for i in range(len(text) - len(pattern) + 1):
        new = text[i:(i+len(pattern))]
        
        if hammingDistance(pattern, new) <= d:
            ret.append(i)

    return ret

def hammingDistance(p: str, q: str) -> int:
    
    i = 0
    count = 0
    
    while i < len(q):
        if p[i] != q[i]:
            count+=1
        i+=1
        
    return count